"""
代码块
"""

from pyscratch.statistician import opcode_dictionary


class Opcode(object):
    """
    代码块的opcode属性
    """

    def __init__(self, opcode: str):
        """
        通过opcode构建opcode对象
        :param opcode: opcode内容
        """
        self.opcode = opcode
        self.category = opcode.split("_")[0]
        self.block_name = opcode.split("_")[1]
        if self.category in opcode_dictionary:
            self.category_cn = opcode_dictionary[self.category]
        else:
            self.category_cn = "其它"

    def __repr__(self):
        # TODO: 美化
        return self.opcode


class Block(object):
    """
    一个代码块
    """

    def __init__(self, block_id: str, block: dict):
        """
        从一个原始代码块构建代码块对象
        :param block: Dict，project.json里面的
        :param block_id: 代码块id
        """
        self.id = block_id
        self.opcode = Opcode(block['opcode'])
        self.next = block['next']
        self.parent = block['parent']
        self.topLevel = block['topLevel']

        if self.topLevel:
            self.x = block['x']
            self.y = block['y']
        else:
            self.x = None
            self.y = None

    def __lt__(self, other):
        return self.parent == other.id

    def __gt__(self, other):
        return self.next == other.id

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        # TODO: 美化
        return f"<Block {self.opcode}>"


class Blocks(object):
    """
    一群代码块
    """

    def __init__(self, blocks: dict):
        """
        根据blocks构建脚本集合
        :param blocks: Blocks
        """
        self.blocks = []
        self.wrong_blocks = []
        for k, v in blocks.items():
            if type(v) == dict:
                try:
                    self.blocks.append(Block(k, v))
                except (KeyError, IndexError):
                    self.wrong_blocks.append((k, v))

    def count_parts(self):
        """
        计算代码块数量
        :return:
        """
        count = 0
        for i in self.blocks:
            if i.topLevel:
                count += 1
        return count

    def __repr__(self):
        return self.blocks.__repr__() + "\n" + f"wrong blocks: {len(self.wrong_blocks)}"

    def __len__(self):
        return len(self.blocks)

    def __iter__(self):
        return self.blocks.__iter__()
