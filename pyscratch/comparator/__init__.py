"""
差异比较
"""

from difflib import SequenceMatcher
from time import time


class Comparator(object):
    """
    判断两个scratch对象的相似度
    """

    def __init__(self, scratch):
        self.scratch = scratch
        self.variables = SequenceMatcher(None, '\n'.join(sorted(scratch.statistic.variables)))
        self.lists = SequenceMatcher(None, '\n'.join(sorted(scratch.statistic.lists)))

        self.matcher = SequenceMatcher(None, scratch.program_json)

    def compare(self, scratch):
        t = time()
        self.variables.set_seq2(
            '\n'.join(sorted(scratch.statistic.variables))
        )
        self.lists.set_seq2(
            '\n'.join(sorted(scratch.statistic.lists))
        )
        self.matcher.set_seq2(
            scratch.program_json
        )
        code_ratio = 0
        s = 0
        for k, v in self.scratch.statistic.category.items():
            if scratch.statistic.category[k] > 30 and v > 30:
                current_ratio = self.compare_number(
                    scratch.statistic.category[k], v)
                code_ratio += current_ratio  # *self.compare_number(
                #    (self.scratch.statistic.category[k]+v)/2,
                #    self.scratch.statistic
                # )
                s += 1
        code_ratio = code_ratio / s

        return {
            'variables': self.variables.ratio(),
            'lists': self.lists.ratio(),
            # 'scratch': self.matcher.ratio(),
            'code': code_ratio,
            'time': time() - t
        }

    @staticmethod
    def compare_number(a: int, b: int):
        """
        比较两个数字的相似性
        0.9以上即为很相近（抄袭）
        """
        return ((1 - abs(a - b) / ((a + b) / 2)) + 1) / 2

    def build(self):
        pass
        # 根据Scratch对象，构建json，去除id等会变的元素，进行比较
