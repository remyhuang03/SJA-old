# 开发者：孤言
# 版本号：0.0.0
# 免责声明：
# 本分析器所提供的分析结果仅供参考。不得作为判定抄袭的直接依据。
# 对滥用本分析器造成的一切后果，作者概不负责。
# 版权声明：
# 未经原作者许可，严禁将该程序用户商业用途。

from tkinter import *

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
lb_title = Label(image=img_title)
lb_title.place(x=-2, y=0)

# 状态侧边选单
class side_btn:
    def show(self, index):
        raw_y = 160;


top.mainloop()
