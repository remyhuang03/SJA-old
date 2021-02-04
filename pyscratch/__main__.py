"""
命令行程序
"""

from tkinter.filedialog import askopenfilename
from pyscratch.loader import load_from_file_path


project = load_from_file_path(askopenfilename())
print(project.report.txt)
