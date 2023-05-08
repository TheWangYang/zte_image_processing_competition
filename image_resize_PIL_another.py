import os
from PIL import Image

# 处理单张图片的函数
def chuli_image(file_path, result_path):
    # 打开图片
    image = Image.open(file_path)
    # 获取图片的宽和高
    width, height = image.size
    # 计算缩放比例
    new_width = None
    new_height = None
    if width < height:
        new_width = 720
        new_height = 1280
    else:
        new_width = 1280
        new_height = 720
    # 缩放图片
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    # 保存图片
    image.save(result_path)



if __name__=="main":
    root_dir = ".\\path to data"
    RESULTS_PATH = ".\\path to results"

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            # 判断文件是否为图片格式
            if file.endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
                # 获取文件的完整路径
                file_path = os.path.join(subdir, file)
                print("subdir: ", subdir)
                item_name = subdir.split('\\')[-1]
                result_path = RESULTS_PATH + "\\" + item_name
                os.makedirs(result_path, exist_ok=True)
                result_path = os.path.join(result_path, file)
                # 处理图片
                chuli_image(file_path, result_path)

