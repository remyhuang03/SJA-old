"""
角色
"""

from pyscratch.scratch.blocks import Blocks


class Sprite(object):
    """
    角色
    """

    def __init__(self, sprite: dict):
        """
        通过角色的JSON构建出角色对象
        :param sprite: Dict类型的角色信息
        """
        self.isStage = sprite['isStage']
        self.name = sprite['name']
        self.variables = list(sprite['variables'].values())
        self.lists = list(sprite['lists'].values())
        self.broadcasts = list(sprite['broadcasts'])  # 广播
        self.blocks = Blocks(sprite['blocks'])
        self.comments = sprite['comments']
        if not self.isStage:
            self.x = sprite['x']
            self.y = sprite['y']
            self.size = sprite['size']
            self.direction = sprite['direction']
            self.draggable = sprite['draggable']

    def __repr__(self):
        return f"<Sprite {self.name} with {len(self.blocks)} blocks>"

    def __iter__(self):
        return self.blocks.__iter__()

    def __len__(self):
        return len(self.blocks)

    # TODO: 角色的统计
