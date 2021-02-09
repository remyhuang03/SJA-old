"""
命令行程序
"""

from tkinter.filedialog import askopenfilename
import sys
import os

from pyscratch.loader import load_from_file_path, load_from_kada
from pyscratch import sja_logo

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


def one():
    """\
分析一个本地scratch3文件
"""
    project = load_from_file_path(askopenfilename())
    print(project.report.txt)


def from_kada():
    """\
从kada上加载一个程序
"""
    project = load_from_kada(input('请输入一个项目地址：'))
    print(project.report.txt)


d = [
    (one.__doc__, one),
    (from_kada.__doc__, from_kada),
]

words = """
欢迎使用本工具
在这里，你可以：
"""


def main():
    print(sja_logo)
    print(words)

    for i in range(len(d)):
        print(f"{i+1}. {d[i][0]}", end='')
    d[int(input('请输入序号来执行：'))-1][1]()
    print()
    input('换行结束程序... ')


main()
