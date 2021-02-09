"""
简单入门教程
"""
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

# TODO: 待补充