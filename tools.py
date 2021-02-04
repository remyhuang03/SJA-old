"""
scratch实用工具集
"""

import requests
import re
from sja import Scratch, NotScratch3Error
from cli import cli, time


def from_kada():
    """
    从kada.163.com中的scratch展示页面中获取project.json
    """
    url = input("url: ")
    html = requests.get(url).content.decode()
    pattern = re.compile(r'steam\.nosdn\.127\.net/\w*\.json')
    target = pattern.search(html)
    if target is None:
        print("在这个页面里没有找到目标网址")
        print(html)
        return
    target = target.group()
    program = requests.get(f"http://{target}").content.decode()
    cli(program)
    sja = Scratch()
    sja.load(program)
    try:
        sja.json_parse()
    except NotScratch3Error:
        print("不是一个scratch3程序！")
    except Exception as e:
        print("错误:", e)
        print("json解析失败，使用re解析")
        sja.re_parse()
    print(sja.codes.category)
    print(sja.codes.blocks)


tools = {
    "from_kada": ("从网络中获取(目前仅支持kada.163.com上的项目，支持闭源项目(后果自负))",
                  from_kada)
}

if __name__ == '__main__':
    for k, v in tools.items():
        print(f"{k}: \t\t{v[0]}")
    tools[input(': ')][1]()
