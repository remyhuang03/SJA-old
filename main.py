# 开发者：孤言
# 版本号：0.0.0
# 免责声明：
# 本分析器所提供的分析结果仅供参考。不得作为判定抄袭的直接依据。
# 对滥用本分析器造成的一切后果，作者概不负责。
# 版权声明：
# 未经原作者许可，严禁将该程序用户商业用途。

from tkinter import *

# 侧边栏宽度：250
# 上边栏宽度：150左右

#菜单被点击函数
def menuclicked():
    pass

# 主窗口
top = Tk()
top.geometry("1024x720+150+0")
top.title("SJA ( V0.0 By孤言 )")
top.iconbitmap("win_icon.ico")
top.config(bg='white')
top.resizable(0, 0)

# 侧边线
cv = Canvas(top, bg='white', width=1024, height=720)
side_line = cv.create_line(250, 130, 250, 690, fill='grey', width=3)
cv.place(x=0, y=0)

# 标题
img_title = PhotoImage(file="fore_title.png")
Label(image=img_title).place(x=-2, y=0)

# 状态侧边选单
img_side_menu = PhotoImage(file="side_menu.png")
Label(image=img_side_menu,bd=0,cmd=menuclicked()).place(x=20, y=160)


top.mainloop()
