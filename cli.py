"""
主程序
"""

from pprint import pprint
from tkinter import filedialog
import time
import json
import webbrowser

from sja.core import Scratch, NotScratch3Error
from sja import __version__, __author__
from sja.highcharts import pie, needs
from sja.report import SjaReport


debug = False


def main():
    """
    主程序，分析scratch3文件
    """
    print(
        "欢迎使用SJA: Scratch Json Analyser\n"
        "这个程序是SJA核心实现\n"
        f"author: {__author__}\n"
        f"version: {__version__}\n"
    )

    print("""\
你可以：
1. 输入一个scratch文件路径，程序会自动分析
2. 输入一个scratch文件的project.json文件内容
3. 输入"choose"来使用图形化界面选择一个文件(新功能！)\
    """)
    file = input('请输入(空输入默认为"choose")\n: ')
    if file == "choose" or file == "" or file == "3":
        file = filedialog.askopenfilename()
    cli(file)


def cli(file=""):
    sja = Scratch()
    t = time.time()
    print()
    print("正在载入...")
    sja.load(file)
    t = time.time() - t
    t2 = time.time()
    print("正在使用json库分析...")
    try:
        sja.json_parse()
    except NotScratch3Error:
        print("不是一个Scratch3文件！")
    print("json库分析完成")
    print()
    print("概述：")
    cn_category = {}
    for i in sja.codes.category:
        cn_category[sja.codes.get_cn_name(code=i)] = sja.codes.category[i]
    pprint(cn_category)
    print()
    print("详细统计：")
    print(json.dumps(sja.codes.blocks, sort_keys=True, indent=2))
    print()
    print(f"载入用时：{round(t, 4)}s")
    print(f"分析用时：{round(time.time() - t2, 4)}s")
    if debug:
        pprint(sja._debug)

    print(pie(SjaReport(file)))


if __name__ == '__main__':
    main()
    input("程序结束 \n\n回车退出... ")
