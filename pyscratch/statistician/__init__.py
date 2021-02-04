"""
统计器
"""

opcode_dictionary = {
    "looks": "外观",
    "control": "控制",
    "motion": "移动",
    "sound": "声音",
    "event": "事件",
    "sensing": "侦测",
    "operator": "运算",
    "procedures": "自定义模块",
    "argument": "模块参数",
    "data": "数据",
    "pen": "画笔",
    "music": "音乐",
    "mistake": "误差",
    "other": "其它",
}


class Statistician(object):
    """
    统计器
    """

    def __init__(self, scratch):
        """
        统计器
        :param scratch: 待统计的scratch对象
        """
        self.filename = scratch.filename
        self.scratch = scratch

        self.variables = []
        self.lists = []
        self.record_variables()

        self.blocks_count = 0
        self.parts_count = 0
        self.blocks_all = []
        self.record_blocks()

        self.category = {}
        self.category_cn = {}
        self.record_category()

        self.percent_cn = {}
        self.percent = {}
        self.percent_corrected = 0
        self.count_percent()

    def record_variables(self):
        self.variables.extend(map(lambda x: x[0], self.scratch.stage.variables))
        self.lists.extend(map(lambda x: x[0], self.scratch.stage.lists))
        for i in self.scratch.sprites:
            self.variables.extend(map(lambda x: x[0], i.variables))
            self.lists.extend(map(lambda x: x[0], i.lists))

    def record_blocks(self):
        self.blocks_count += len(self.scratch.stage.blocks)
        self.blocks_all.extend(self.scratch.stage.blocks.blocks)
        self.parts_count += self.scratch.stage.blocks.count_parts()
        for i in self.scratch.sprites:
            self.blocks_count += len(i.blocks)
            self.blocks_all.extend(i.blocks.blocks)
            self.parts_count += i.blocks.count_parts()

    def record_category(self):
        for i in opcode_dictionary.keys():
            self.category[i] = 0
        for i in opcode_dictionary.values():
            self.category_cn[i] = 0

        for i in self.blocks_all:
            if i.opcode.category in opcode_dictionary.keys():
                self.category[i.opcode.category] += 1
            else:
                self.category['other'] += 1
            if i.opcode.category_cn in opcode_dictionary.values():
                self.category_cn[i.opcode.category_cn] += 1

    def count_percent(self):
        percent = {}
        for k, v in self.category.items():
            if self.blocks_count > 0:
                percent[k] = round(v / self.blocks_count * 10000)
        corrected = 10000 - sum(percent.values())
        percent['mistake'] = corrected
        self.percent_corrected = corrected / 100

        for k, v in percent.items():
            self.percent[k] = v / 100
            self.percent_cn[opcode_dictionary[k]] = v / 100

    def __repr__(self):
        return f'<Scratch file "{self.scratch.filename}" with {self.blocks_count} blocks>'
