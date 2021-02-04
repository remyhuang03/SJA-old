"""
命令行程序
"""

from tkinter.filedialog import askopenfilename

from pyscratch.loader import load_from_file_path

from pyscratch import sja_logo


def one():
    """\
分析一个本地scratch3文件
    """
    project = load_from_file_path(askopenfilename())
    print(project.report.txt)


d = [
    (one.__doc__, one)
]

words = """
欢迎使用本工具
在这里，你可以：
"""


def main():
    print(sja_logo)
    print(words)

    for i in range(len(d)):
        print(f"{i+1}. {d[i][0]}")
    d[int(input('请输入序号来执行：'))-1][1]()
    print()
    input('换行结束程序... ')


main()
