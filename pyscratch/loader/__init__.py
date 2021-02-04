"""
加载器
"""

from zipfile import ZipFile
from os.path import basename

from time import time
from pyscratch.scratch import Scratch


def load_from_str(program: str):
    """
    从程序JSON构建
    :param program: 程序的project.json
    :return: 对应的Scratch对象
    """
    scratch = Scratch(program)
    return scratch


def load_from_file_path(file_path: str):
    """
    从scratch3项目文件构建
    :param file_path: 文件路径
    :return: 对应的Scratch对象
    """
    t = time()
    f = ZipFile(file_path)
    file = f.read("project.json").decode()
    f.close()
    load_time = time() - t
    scratch = Scratch(file)
    scratch.load_time += load_time
    scratch.filename = basename(file_path)
    return scratch


def load_from_bytes(file):
    """
    从二进制文件构建
    :param file: 可读取的二进制文件对象
    :return: 对应的scratch对象
    """
    t = time()
    project = ZipFile(file)
    file = project.read("project.json").decode()
    load_time = time() - t
    scratch = load_from_str(file)
    scratch.load_time += load_time
    return scratch

# TODO: 更多加载方式
