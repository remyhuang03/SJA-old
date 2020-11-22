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

# 菜单图片字典
menu_dic = {0: 'add_file', 1: 'report', 2: 'setting'}

menu_chosen = 0
def menuclicked(event):  # 菜单被点击函数
    global menu_chosen
    y=event.y # 菜单：160-200(加载文件), 240-300（分析报告）,340-400（设置）

    is_chson = FALSE

    # ✨判断菜单出现位置
    if 160<=y<=200:
        menu_chosen=0
        is_chson = TRUE
    elif 240<=y<=300:
        menu_chosen=1
        is_chson = TRUE
    elif 340<=y<=400:
        menu_chosen=2
        is_chson = TRUE

    if is_chson:
        refresh_interface(menu_chosen)


# 主窗口
top = Tk()
top.geometry("1024x720+150+0")
top.title("SJA ( V0.0 By孤言 )")
top.iconbitmap("win_icon.ico")
top.config(bg='white')
top.resizable(0, 0)

# 侧边线
cv = Canvas(top, bg='white', width=1024, height=720)
cv.create_line(250, 130, 250, 690, fill='grey', width=3)
cv.place(x=0, y=0)

# 标题
img_title = PhotoImage(file="fore_title.png")
Label(image=img_title).place(x=-2, y=0)

# 状态侧边选单
img_side_menu = PhotoImage(file="side_menu.png")
menu = Label(image=img_side_menu, bd=0)
menu.place(x=20, y=160)
menu.bind('<Button-1>', menuclicked)

top.mainloop()
