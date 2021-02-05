"""
单元测试
"""

from tests import unittest
import os
from zipfile import ZipFile

from pyscratch.loader import \
    load_from_file_path, load_from_str, load_from_bytes, load_from_kada

example_path = os.path.join(os.path.dirname(__file__), '../examples/example.sb3')
example_path_copy = os.path.join(os.path.dirname(__file__), '../examples/example抄袭版.sb3')
example_big_scratch_file_path = r'D:\scratch\Flight Simulator 3D v2.8.sb3'
example_project_url1 = 'https://kada.163.com/project/5867314-4110299.htm'
example_project_url2 = 'https://kada.163.com/project/5966352-3592155.htm'
example_project_url3 = 'https://kada.163.com/project/4528433-3333623.htm'


class PyScratchTestCase(unittest.TestCase):
    def test_loader(self):
        f = open(example_path, 'rb')
        zipfile = ZipFile(example_path)
        s = zipfile.read('project.json').decode()

        p1 = load_from_file_path(example_path)
        p2 = load_from_str(s)
        p3 = load_from_bytes(f)

        zipfile.close()
        f.close()

        self.assertEqual(p1.statistic.category, p2.statistic.category)
        self.assertEqual(p3.statistic.category, p2.statistic.category)
        self.assertEqual(p1.statistic.parts_count, p2.statistic.parts_count)
        self.assertEqual(p3.statistic.parts_count, p2.statistic.parts_count)

    def test_scratch(self):
        scratch = load_from_file_path(example_path)

        self.assertIsNot(scratch, None)
        self.assertEqual(scratch.filename, 'example.sb3')
        self.assertIn('other', scratch.statistic.category)
        self.assertIn('事件', scratch.statistic.percent_cn)
        self.assertEqual(100.0, round(sum(scratch.statistic.percent.values()), 2))
        self.assertEqual(len(scratch.statistic.blocks_all), scratch.statistic.blocks_count)

        print(scratch.statistic.category_cn)
        print(scratch.statistic.blocks_count)
        print(scratch.statistic.parts_count)
        print(scratch.load_time)
        print(scratch.build_time)

    def test_comparator(self):
        project = load_from_file_path(example_path)
        project_copy = load_from_file_path(example_path_copy)
        x = project.comparator.compare(project_copy)
        print(x)
        self.assertTrue(x['code'] > 0.8)

    def test_api(self):
        project = load_from_file_path(example_big_scratch_file_path)
        x = 0
        for i in project:
            print(i)
            for j in i:
                x += 1
        print(project.stage)
        print(project.stage.name)
        x = x + len(project.stage.blocks)
        print(x)
        self.assertEqual(x, project.statistic.blocks_count)
        print(project)
        print(project.sprites)
        print(project.filename)

    def test_load_from_kada(self):
        try:
            print("下载项目1...")
            project1 = load_from_kada(example_project_url1)
            # print("下载项目2...")
            # project2 = load_from_kada(example_project_url2)
            # print("下载项目3...")
            # project3 = load_from_kada(example_project_url3)
            # print("比较...")
            # x1 = project1.comparator.compare(project2)
            # x2 = project3.comparator.compare(project2)
            # self.assertTrue(x1['code'] > 0.8)
            self.assertIn('事件', project1.report.txt)
            # print("两个已知抄袭的作品的相似度:", x1)
            # print("半毛钱关系都没有的相似度:", x2)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    unittest.main()
