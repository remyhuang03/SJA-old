r"""
PyScratch

食用方法：
from pyscratch.loader import load_from_file_path
# pyscratch.loader提供了许多加载scratch文件的方法，常用的是load_from_file_path
# 这个函数会返回一个scratch对象(pyscratch.scratch.Scratch)，Scratch对象是这个项目的核心
# 许多scratch有关的数据都存储在这里
project = load_from_file_path('/path/to/example.sb3')    # 请根据实际需求替换文件路径

print(dir(project))
# 列举出Scratch提供的属性和方法
# 可以看到，有一个statistic，输出看看有什么信息
print(project.statistic)
# 再看一看statistic提供了哪些方法和属性
print(dir(project.statistic))
......
详细信息请见
tutorial.py
"""

author = ['kunkun']
__version__ = '2.1.1'

pyscratch_logo = r"""
 ____        ____                 _       _
|  _ \ _   _/ ___|  ___ _ __ __ _| |_ ___| |__
| |_) | | | \___ \ / __| '__/ _` | __/ __| '_ \
|  __/| |_| |___) | (__| | | (_| | || (__| | | |
|_|    \__, |____/ \___|_|  \__,_|\__\___|_| |_|
       |___/

"""

sja_logo = r"""
 ____      _   _
/ ___|    | | / \
\___ \ _  | |/ _ \
 ___) | |_| / ___ \
|____/ \___/_/   \_\
"""
