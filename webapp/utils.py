"""
辅助函数
"""

from pyscratch.loader import load_from_bytes
from werkzeug.datastructures import FileStorage

from uuid import uuid4


class UploadedScratch(object):
    def __init__(self, upload):
        project1 = None
        project2 = None
        upload: FileStorage
