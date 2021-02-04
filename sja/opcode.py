"""
opcode对象。可以对opcode进行分析和记录。
"""

import re


class Opcode(object):
    """
    opcode对象。可以对opcode进行分析和记录。
    """
    # 通过opcode的特征进行积木分类
    opcodes = {
        "looks": "外观",
        "control": "控制",
        "motion": "移动",
        "sound": "声音",
        "event": "事件",
        "sensing": "侦测",
        "operator": "运算",
        "procedures": "自定义",
        "argument": "参数",
        "data": "数据",
        "other": "其它",
    }

    def __init__(self):
        self.blocks = {}  # 具体方块名称
        self.category = {}  # 各个类别方块数量
        for i in self.opcodes.keys():
            self.category[i] = 0
        self.err = []

    def parse(self, code=""):
        """
        传入opcode，返回它的类型与具体标识
        """
        other = {
            "note": "unknown"
        }
        if code not in other:
            pattern = re.compile(r'[a-z]+_[a-z]+')
            match = pattern.search(code)
            if not match:
                self.err.append(("code", "unknown"))
            match = match.group()
            return match.split("_")
        return 'other', 'note'

    def record(self, code):
        """
        opcode的记录与存储
        """
        # 记录blocks
        codes = self.parse(code)
        if codes[0] not in self.blocks.keys():  # 初始化这个类别
            self.blocks[codes[0]] = {}
        if codes[1] not in self.blocks[codes[0]].keys():  # 初始化这个方块
            self.blocks[codes[0]][codes[1]] = 0
        self.blocks[codes[0]][codes[1]] += 1  # 这个类别下，这个方块又多了一个

        # 记录category
        if codes[0] in self.category.keys():
            self.category[codes[0]] += 1
        else:
            self.err.append((codes[0], "unknown"))

    def get_cn_name(self, code):
        """
        获取一个分类的中文名
        """
        if code in self.opcodes:
            return self.opcodes[code]
        else:
            return "其它"

    def get_sum(self):
        return sum(self.category.values())

