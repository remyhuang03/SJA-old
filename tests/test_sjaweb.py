"""
测试套件
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from requests import head
from requests.exceptions import ConnectTimeout

from webapp.models import DataDict
from webapp import make_app

import os
from sja.report import SjaReport
from time import sleep, time
import unittest

app = make_app('testing')


class SjawebTestCase(unittest.TestCase):

    def setUp(self):
        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()

    def test_app_status(self):
        self.assertTrue(app is not None)
        self.assertTrue(app.config['TESTING'])

    def test_404_page(self):
        response = self.client.get("/nothing/but/404")
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn('404', data)
        self.assertIn('返回分析器', data)

    def test_pages(self):
        print("测试常见页面...")
        pages = {
            "/": ['文件上传', "小提示", "查看结果",
                  "关于", "核心版本", "Scratch程序分析器", "kunkun"
                  "https://gitee.com/gitkunkun/sja-bin",
                  "http://127.0.0.1:5000/load_url",
                  "https://kada.163.com/project/v3/create.htm?utm_source=&utm_medium=nav_button&utm_campaign=business"
                  "&utm_content=sc ",
                  "https://github.com/kunkunhub",
                  "https://github.com/GuYan1024/SJA",
                  "https://gitee.com/gitkunkun/sjaweb"
                  ],
            "/help": ["帮助", "scratch分析器", "下载", "scratch3", "如何", "为什么", "返回分析器"],
            "/about": ["帮助", "scratch分析器", "下载", "主要维护者", "返回分析器"],
            "/load_url": ["kada网址", "帮助", "scratch分析器", "下载", "确定"],
            # 导航栏
        }
        for i in pages.keys():
            response = self.client.get(i)
            data = response.get_data(as_text=True)
            self.assertTrue(response.status_code == 200)
            for j in pages[i]:
                self.assertIn(i, data)
        print("完成")

    def test_DataDict(self):
        print("测试DataDict")
        db = DataDict(timeout=0.1)
        db['a'] = 1
        db['b'] = 2
        sleep(0.15)
        db['c'] = 3
        self.assertIn('c', db)
        self.assertNotIn('a', db)
        self.assertNotIn('b', db)
        db['d'] = 4
        self.assertEqual(db['c'], 3)
        self.assertEqual(db['d'], 4)
        self.assertEqual(len(db), 2)
        sleep(0.15)
        db.update()
        self.assertEqual(len(db), 0)
        print("完成")

    def tearDown(self):
        self.context.pop()


class UserInterfaceTestCase(unittest.TestCase):
    def setUp(self):
        print("UI测试准备中...")
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.client = webdriver.Chrome(options=options)

        if not self.client:
            self.skipTest('Web browser not available.')

        try:
            response = head("http://127.0.0.1:5000", timeout=0.1)
        except ConnectTimeout:
            self.skipTest("Flask server isn't running.")
        print("UI测试开始")

    def test_help(self):
        print("测试帮助页面")
        self.client.get('http://127.0.0.1:5000/')
        sleep(0.1)
        self.client.find_element_by_link_text("帮助").click()
        sleep(0.1)
        self.assertIn("为什么", self.client.page_source)
        print("完成")

    def test_index(self):
        # tips
        print("测试小提示...")
        for i in range(10):
            self.client.get('http://127.0.0.1:5000/')
            sleep(0.1)
            if "这个分析器只能分析scratch3文件！" in self.client.page_source:
                print("成功")
                break
        else:
            self.assertTrue(False, msg='找不到 "这个分析器只能分析scratch3文件！" 的小提示')

        # other
        print("测试其它部件")
        self.client.find_element_by_link_text('scratch分析器').click()
        sleep(0.1)
        self.assertIn("scratch3文件上传", self.client.page_source)
        self.client.find_element_by_id("check_report").click()
        sleep(0.1)
        self.assertIn('请先上传', self.client.page_source)
        print("完成")

    def test_load_url(self):
        print("测试从kada载入...")
        self.client.get('http://127.0.0.1:5000/load_url')
        sleep(0.1)
        self.assertIn("从kada社区加载", self.client.page_source)
        item_input = self.client.find_element_by_id('url')
        item_input.send_keys('https://kada.163.com/project/3704335-26018.htm')
        item_input.send_keys(Keys.RETURN)
        print("输入完毕")
        sleep(1)
        self.assertIn('分析结果', self.client.page_source)
        print("成功")
        self.client.find_element_by_link_text("返回分析器").click()
        sleep(0.1)
        self.assertIn("小提示", self.client.page_source)
        print("完成")

    def tearDown(self):
        if self.client:
            self.client.quit()


if __name__ == "__main__":
    unittest.main()
