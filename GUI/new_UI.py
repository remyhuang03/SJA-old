import pygame
import os
import sys
from tkinter import filedialog
import tkinter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from pyscratch.loader import load_from_file_path

__author__ = ['GuYan1024', 'kunkun', 'sun-xx']


def draw_line(start_pos, end_pos, rgb, thickness):
    pygame.draw.line(screen, rgb, start_pos, end_pos, thickness)
    pygame.display.update()


def analysis(path):
    global project
    try:
        project = load_from_file_path(path)
    except Exception as msg:
        print(f'Error: {msg}')

    global reported
    reported = 1  # 已分析


def update(focus):  # 切换界面
    screen.fill(WHITE)
    title = pygame.image.load('.\\fore_title.png')  # 各种贴图
    screen.blit(title, (-200, 0))  # 标题
    add_file = pygame.image.load('.\\add_file.png')
    screen.blit(add_file, (0, 120))  # 加载
    report = pygame.image.load('.\\report.png')
    screen.blit(report, (0, 200))  # 报告
    # 画分割线
    start_pos = 280, 120  # 分割线开始坐标
    end_pos = 280, 580  # 分割线结束坐标
    draw_line(start_pos, end_pos, (128, 138, 135), 3)
    global reported  # 使用全局变量 是否加载

    if focus == 'add_file':  # 加载文件
        screen.blit(pygame.image.load('.\\add_file_chosen.png'), (0, 120))
        screen.blit(pygame.image.load('.\\button.png'), (450, 200))
    elif focus == 'report':  # 查看报告
        screen.blit(pygame.image.load('.\\report_chosen.png'), (0, 200))
        if reported == 1:
            # 放背景
            screen.blit(pygame.image.load('.\\report_background.png'), (300, 120))
            # 渲染积木数量
            blocks_num = project.statistic.blocks_count
            font = pygame.font.Font(None, 30)
            blue = 98, 0, 238
            text = font.render(str(blocks_num), True, blue)
            screen.blit(text, (450, 208))

            # 渲染积木百分比
            keys = ('移动', '外观', '声音', '事件', '控制', '侦测',
                    '运算', '数据', '画笔', '自定义模块', '其它')
            start_pos = [380, 290]
            rgbs = [(87, 143, 223), (157, 107, 255), (221, 119, 221),
                    (255, 214, 19), (255, 187, 70), (78, 192, 230),
                    (78, 195, 87), (255, 160, 67), (96, 134, 214),
                    (255, 94, 121), (160, 160, 160)]
            for i in range(0, 6):
                '''
                分类块数
                print(keys[i] + ':', project.statistic.category_cn[keys[i]])
                分类百分比
                print(str(project.statistic.percent_cn[keys[i]]) + '%')
                '''
                start_pos[1] += 30
                if (start_pos[0] + (project.statistic.percent_cn[keys[i]]) * 5) > 550:
                    end_pos = [550, start_pos[1]]
                else:
                    end_pos = [start_pos[0] + (project.statistic.percent_cn[keys[i]]) * 5, start_pos[1]]
                draw_line(start_pos, end_pos, rgbs[i], 5)
            start_pos = [630, 290]
            for i in range(7, 12):
                start_pos[1] += 30
                end_pos = [start_pos[0] + (project.statistic.percent_cn[keys[i - 1]]) * 5, start_pos[1]]
                draw_line(start_pos, end_pos, rgbs[i - 1], 5)
        else:
            # 没加载就看报告?找抽呢你!
            screen.blit(pygame.image.load('.\\no_report.png'), (350, 200))

    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    root = tkinter.Tk()
    root.withdraw()

    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('SJA ( V0.0 By孤言 )')  # 启动窗口

    win_icon = pygame.image.load('.\\win_icon.png')
    pygame.display.set_icon(win_icon)  # 孤言头像(好好看啊)

    WHITE = (255, 255, 255)  # 白色背景
    screen.fill(WHITE)

    reported = 0  # 未分析
    update(focus='add_file')  # 放置按钮
    state = 'add_file'
    while True:  # 主循环
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:  # 按ESC键退出
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if e.type == pygame.QUIT:  # 按关闭按钮退出
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:  # 鼠标事件
                pos = pygame.mouse.get_pos()  # 获取鼠标坐标
                # print(pos)  # 测试用
                if 0 < pos[0] < 250 and 120 < pos[1] < 180:
                    update(focus='add_file')  # 按下选择文件
                    state = 'add_file'
                elif 0 < pos[0] < 250 and 210 < pos[1] < 270:
                    update(focus='report')  # 按下报告
                    state = 'report'
                elif 0 < pos[0] < 250 and 290 < pos[1] < 360:
                    update(focus='setting')  # 按下设置
                    state = 'setting'
                elif 470 < pos[0] < 620 and 190 < pos[1] < 350:
                    if state == 'add_file':  # 选择文件
                        file_name = filedialog.askopenfilename()
                        analysis(file_name)
