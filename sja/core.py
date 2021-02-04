"""
分析器
"""


import re
import json
import zipfile
import os
from sja.opcode import Opcode
from sja.errors import NotScratch3Error


class Scratch(object):
    """
    一个scratch程序解析对象
    解析方式：
    1. 实例化这个类
    2. 使用load方式载入程序(project.json或程序路径)
    3. 调用re_parse方法解析程序(使用正则表达式)
    4. 结果会存在codes里面
    各个函数具体使用方法参见各自的说明
    """

    def __init__(self):
        """
        初始化，无需参数
        """
        # 存储不同类型代码块的出现次数
        self.codes = Opcode()
        self.program = ""
        self._debug = {'json': []}
        self.unknown = []  # 错误信息
        self.progpy = ""
        self.thread = None

    def load(self, program=""):
        """
        载入程序，无返回值
        program: 如果是一个文件的路径(str类型)，将会尝试以zip格式打开并自动提取project.json
        否则变量内容应为project.json完整内容，str类型。
        """
        try:
            if not os.path.isfile(program):
                self.program = program
                return
        except TypeError:
            pass
        try:
            sb3_file = zipfile.ZipFile(program)
        except zipfile.BadZipfile:
            print(f"File is not a scratch3 file")
            raise
        if "project.json" not in sb3_file.namelist():
            raise FileNotFoundError(f"Cannot find project.json file in this scratch file ")
        self.program = sb3_file.open("project.json").read().decode()
        sb3_file.close()

    def re_parse(self):
        """
        解析程序，无参数，无返回值
        使用正则表达式解析
        """
        if "targets" not in self.program:
            raise NotScratch3Error("Not a scratch3 program")
        self.clean()
        pattern = r'"opcode":\s?"[a-z]+_[a-z_]+",'
        # 使用正则找到某种分类的积木个数，并存到codes字典里面。
        code_blocks = re.findall(pattern, self.program)
        for i in range(len(code_blocks)):
            self.codes.record(code_blocks[i])
        self._debug['opcode'] = self.codes.err
        # self._debug[i] = re.findall(pattern, self.program)

    def json_parse(self):
        """
        解析程序，无参数，无返回值
        用json库解析
        """
        self.clean()
        # 把json转换成python类型
        try:
            self.progpy = json.loads(self.program)
            if "targets" not in self.progpy:
                raise NotScratch3Error("Not a scratch3 program")
            # 我的天那这json一层一层的真是太不像话了
            # j遍历角色，i遍历代码块
            for j in self.progpy['targets']:
                if not j["isStage"]:
                    for i in j["blocks"]:
                        try:
                            self.codes.record(j["blocks"][i]["opcode"])
                        except TypeError:
                            self._debug['json'].append((j["blocks"][i], 'TypeError'))
        except json.decoder.JSONDecodeError as err_info:
            raise NotScratch3Error(
                f"An exception occurred while parsing: {err_info} \n"
                f"This may be because the project.json file is not a correct scratch3 program"
            )

    def clean(self):
        """
        清空codes
        """
        self.codes = Opcode()
