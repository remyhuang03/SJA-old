# 开发者：孤言、kunkun
# 免责声明：
# 本分析器所提供的分析结果仅供参考。不得作为判定抄袭的直接依据。
# 对滥用本分析器造成的一切后果，作者概不负责。
# 版权声明：
# 未经原作者许可，严禁将该程序用户商业用途。

__version__ = "0.0.0"
__author__ = ["GuYan", "kunkun"]

from tkinter import *

# 侧边栏宽度：250
# 上边栏宽度：150左右

# 主窗口
top = Tk()
top.geometry("1024x720+150+0")
top.title("SJA ( V0.0 By孤言 )")
top.iconbitmap("win_icon.ico")
top.config(bg='white')
top.resizable(0, 0)

cv = Canvas(top, bg='white', width=1024, height=720)

# 标题
imgBuffer = PhotoImage(file="fore_title.png")
Label(image=imgBuffer).place(x=-2, y=0)

# 菜单图片字典
menuDic = {0: 'add_file', 1: 'report', 2: 'setting'}


def chosen(index):
    pass  # 待修改


# 显示侧边按钮
sideImg1 = PhotoImage(file="add_file.png")
sideImg2 = PhotoImage(file="report.png")
sideImg3 = PhotoImage(file="setting.png")

sideBtn1 = Label(image=sideImg1)
sideBtn2 = Label(image=sideImg2)
sideBtn3 = Label(image=sideImg3)

sideBtn1.place(x=0, y=130)
sideBtn2.place(x=0, y=210)
sideBtn3.place(x=0, y=290)

# 侧边线
cv.create_line(280, 130, 280, 690, fill='grey', width=3)
cv.place(x=0, y=0)

top.mainloop()
