
# 解析json的方式
# 1. 正则表达式查找
import re

# 2. json 库解析
import json


# 通过opcode的特征进行积木分类
# TODO: 待完善
opcode = {
    "looks": "外观",
    "control": "控制",
    "motion": "移动"
}


class Scratch:
    """
    一个scratch程序解析对象
    解析方式：
    1. 实例化这个类
    2. 使用load方式载入程序(project.json)(未来会出现自动解压缩包)
    3. 调用re_parse方法解析程序(使用正则表达式)
    4. 结果会存在codes里面
    各个函数具体使用方法参见各自的说明
    """
    def __init__(self):
        """
        初始化，无需参数
        """
        # 存储不同类型代码块的出现次数
        self.codes = {}
        for i in opcode.keys():
            self.codes[i] = 0   # 初始为0
        self.program = ""
        self._debug = {}

    def load(self, program=""):
        """
        载入程序，无返回值
        program: project.json的完整内容，应为str类型

        TODO: 自动解压并提取project.json
        """
        self.program = program

    def re_parse(self):
        """
        解析程序，无参数，无返回值
        使用正则表达式解析，json_parse会使用json模块解析(未来加入)
        """
        for i in opcode.keys():
            pattern = f'"opcode":"{i}_'
            # 使用正则找到某种分类的积木个数，并存到codes字典里面。
            self.codes[i] = len(re.findall(pattern, self.program))
            self._debug[i] = pattern

    def json_parse(self):
        """
        TODO: 使用json模块解析
        此方法暂时不可用，请使用re_parse！
        """
        pass


if __name__ == "__main__":
    prog = Scratch()
    prog.load(input("请输入project.json(尽量只有一行)：\n"))
    prog.re_parse()
    print(prog.codes)
