"""
数据库（高仿）
"""

from time import time
from pprint import pprint


class DataDict:
    """
    键值数据库
    """

    def __init__(self, timeout=300):
        self.dict = {}
        self.timeout = timeout

    def __setitem__(self, key, value):
        self.update()
        self.dict[key] = (value, time())

    def __getitem__(self, key):
        return self.dict[key][0]

    def __delitem__(self, key):
        del self.dict[key]

    def __contains__(self, item):
        return item in self.dict

    def __len__(self):
        return len(self.dict)

    def __repr__(self):
        d = {}
        for k, v in self.dict.items():
            d[k] = v[0]
        return d.__repr__()

    def update(self):
        t = time()
        tmp = []
        for k, v in self.dict.items():
            if t - v[1] > self.timeout:
                tmp.append(k)

        for i in tmp:
            del self.dict[i]


if __name__ == '__main__':
    pass
