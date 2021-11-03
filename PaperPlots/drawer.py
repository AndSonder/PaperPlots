import matplotlib.pyplot as plt
import pandas
import os


class BasicDrawer:
    def __init__(self, style='ieee'):
        plt.style.use(style)


class LineDrawer(BasicDrawer):
    """
    绘制折线图
    """

    def __init__(self, x_name='x', y_name='y', output_path='./output.svg', style='ieee', title=''):
        super(LineDrawer, self).__init__(style)
        self.x_name = x_name
        self.y_name = y_name
        self.output_path = output_path
        self.title = title
        self.pparam = dict(xlabel=self.x_name, ylabel=self.y_name)

    def draw_from_folder(self, folder_path, file_type='csv', save=True):
        """
        将一个文件夹中的csv或者excel进行绘制
        :param folder_path: 文件夹地址
        :param file_type: 数据类型 csv/excel
        :param save: 是否保存，如果设置为False则会调用plt.show()
        """
        file_names = os.listdir(folder_path)
        file_paths = [os.path.join(folder_path, item) for item in file_names]
        file_names = [name.split('.')[0] for name in file_names]
        fig, ax = plt.subplots()
        ax.set(**self.pparam)
        for i, file_path in enumerate(file_paths):
            if file_type == 'csv':
                data = pandas.read_csv(file_path)
            else:
                data = pandas.read_excel(file_path)
            data.dropna()
            columns = data.columns.values
            x = list(data[columns[0]])
            y = list(data[columns[1]])
            ax.plot(x, y, label=file_names[i])
        ax.legend(title=self.title)
        ax.autoscale(tight=True)
        if save:
            fig.savefig(self.output_path)
        else:
            plt.show()


if __name__ == '__main__':
    # drawer = BasicDrawer(['science', 'ieee'])
    pass
