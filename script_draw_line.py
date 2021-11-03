"""
绘制论文实验需要的柱形图，搭配tensorboard使用效果更佳哦
"""

from PaperPlots import LineDrawer

# 数据所在文件夹
folder_path = './test_code'
# 横坐标，可以使用latex语法
x_name = '$Step$'
# 纵坐标，可以使用latex语法
y_name = '$ASR$'
# 图片输出路径
output_path = './output.svg'
style = ['science', 'ieee', 'grid', 'cjk-sc-font']

if __name__ == '__main__':
    drawer = LineDrawer(x_name, y_name, output_path, style=style)
    drawer.draw_from_folder(folder_path, file_type='csv')
