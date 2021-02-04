"""
报告
"""

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    pass

from pyscratch.reporter.highcharts import pie, full_html_pie


class Reporter(object):
    """
    各种结果的呈现方式
    """

    def __init__(self, scratch):
        self.scratch = scratch
        self.plt = None
        self.plot()
        self.pie_html = pie(scratch)
        self.full_html_pie = full_html_pie(scratch)

        self.txt = []
        self.text()

    def plot(self):
        """
        使用matplotlib渲染结果
        :return: None
        """
        if "plt" not in globals():
            raise ModuleNotFoundError("Matplotlib not found.")
        plt.rcParams['font.sans-serif'] = 'SimHei'
        plt.figure(figsize=(6, 6))
        labels = []
        tmp = list(self.scratch.statistic.category_cn.keys())
        tmp.sort()
        values = []
        for i in tmp:
            if self.scratch.statistic.category_cn[i] != 0:
                labels.append(i)
                values.append(self.scratch.statistic.category_cn[i])

        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title(f"{self.scratch.filename}分析报告\n"
                  f"总共{self.scratch.statistic.blocks_count}块")
        self.plt = plt

    def text(self, width=60):
        """
        :return: None
        """
        text = []
        label = list(self.scratch.statistic.percent_cn.keys())
        label.sort(key=lambda x: self.scratch.statistic.percent_cn[x], reverse=True)
        for i in label:
            text.append(
                # f": {(10-len(i))*' '}"
                f"[{'=' * round(width * self.scratch.statistic.percent_cn[i] / 100)}"
                f"{' ' * round(width * self.scratch.statistic.percent_cn[i] / 100)}]  {i}"
                f" {self.scratch.statistic.category_cn[i]}  "
                f"{round(self.scratch.statistic.percent_cn[i], 1)}%"
            )
        text.append(f"文件名：{self.scratch.filename}")
        text.append(f"总块数：{self.scratch.statistic.blocks_count}")
        text.append(f"分析用时：{self.scratch.load_time}")
        #        text.append(f"分析用时：{self.scratch.load_time + self.scratch.build_time}")
        self.txt = "\n".join(text)
