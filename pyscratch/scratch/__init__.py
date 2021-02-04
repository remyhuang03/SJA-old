"""
scratch
"""

from time import time
import json

from pyscratch.scratch.stage import Sprite, Stage

from pyscratch.statistician import Statistician
from pyscratch.comparator import Comparator
from pyscratch.reporter import Reporter


class Scratch(object):
    """
    Oh my Scratch in Python!
    """

    def __init__(self, program_json: str):
        t = time()

        self.program = json.loads(program_json)
        self.program_json = program_json
        self.sprites = []
        self.filename = '<Unnamed>'

        for i in self.program['targets']:
            if i['isStage']:
                self.stage = Stage(i)
            else:
                self.sprites.append(Sprite(i))

        self.load_time = 0
        self.build_time = time() - t

        self.statistic = Statistician(self)
        self.comparator = Comparator(self)
        self.report = Reporter(self)

    def __iter__(self):
        return self.sprites.__iter__()

    def __repr__(self):
        return f'<Scratch file "{self.filename}", {len(self.sprites)}>'


if __name__ == "__main__":
    pass
