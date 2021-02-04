"""
显示结果
"""

from sja.report import SjaReport


try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    pass


class Show(object):
    def __init__(self, program: SjaReport):
        """
        传入SjaReport对象
        """
        self.program = program

    def plot(self):
        """
        使用matplotlib渲染结果
        :return: matplotlib.pyplot.pie对象，使用.show方法展示，.savefig方法保存
        """
        if "plt" not in globals():
            raise ModuleNotFoundError("Matplotlib not found.")
        plt.rcParams['font.sans-serif'] = 'SimHei'
        plt.figure(figsize=(6, 6))
        labels = []
        tmp = list(self.program.category_cn.keys())
        tmp.sort()
        values = []
        for i in tmp:
            if self.program.category_cn[i] != 0:
                labels.append(i)
                values.append(self.program.category_cn[i])

        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title(f"{self.program.program_name}分析报告\n"
                  f"总共{self.program.block_count}块")
        return plt

    def text(self, width=60):
        class ShowText(object):
            text = []
            label = list(self.program.percent_cn.keys())
            label.sort(key=lambda x: self.program.percent_cn[x], reverse=True)
            values = []
            for i in label:
                text.append(
                    f"{i}:\t[{'=' * round(width * self.program.percent_cn[i]/100)}"
                    f"{' ' * round(width * self.program.percent_cn[i]/100)}]"
                    f" {self.program.category_cn[i]}  "
                    f"{round(self.program.percent_cn[i]/100, 1)}%"
                )
            text.append(f"文件名：{self.program.program_name}")
            text.append(f"总块数：{self.program.block_count}")
            text.append(f"分析用时：{self.program.load_time + self.program.parse_time}")

            def savefig(self, path):
                f = open(path, "w")
                f.write("\n".join(self.text))
                f.close()

            def show(self):
                print("\n".join(self.text))

        return ShowText()


