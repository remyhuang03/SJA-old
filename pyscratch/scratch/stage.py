"""
舞台
"""

from pyscratch.scratch.sprites import Sprite


class Stage(Sprite):
    """
    舞台
    """

    def __repr__(self):
        return f"<Stage with {len(self.blocks)} blocks>"
