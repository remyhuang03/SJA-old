"""
分析器包装
"""


from time import time
from sja import __version__
from sja.core import Scratch
import os


class SjaReport(object):
    """
    Scratch类分析结果的总结
    """

    def __init__(self, program: str, name=""):
        """
        传入一个能被core.Scratch.load方法使用的对象(程序路径或程序的project.json)
        """
        self.load_time = time()
        sja = Scratch()
        sja.load(program)
        self.load_time = time()-self.load_time

        self.parse_time = time()
        sja.re_parse()
        self.parse_time = time() - self.parse_time

        self.block_count = sja.codes.get_sum()
        self.blocks = sja.codes.blocks
        self.category = sja.codes.category
        self.category_cn = {}
        self.program = program
        self.core_version = __version__
        self.sja = sja
        self.percent = {}
        self.percent_cn = {}

        for i, v in self.category.items():
            self.category_cn[sja.codes.get_cn_name(i)] = v
            try:
                self.percent[i] = round(v/self.block_count*100, 2)
                self.percent_cn[sja.codes.get_cn_name(i)] = round(v/self.block_count*100, 2)
            except ZeroDivisionError:
                self.percent[i] = 0
                self.percent_cn[sja.codes.get_cn_name(i)] = 0

        try:
            if name:
                self.program_name = name
            elif os.path.isfile(program):
                self.program_name = os.path.basename(program)
            else:
                self.program_name = "Unnamed file"
        except TypeError:
            self.program_name = "Unnamed file"

    def __repr__(self):
        return self.__dict__.__repr__()
