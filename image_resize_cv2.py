import cv2
import os

# 定义目标长宽
MAX_LENGTH = 1280
MAX_SHORT = 720
RESULTS_PATH = ".\\results\\2023050701"

# 遍历目录下的所有文件
def process_files(root_dir):
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
                process_image(file_path, result_path, item_name)

# 处理单张图片
def process_image(file_path, result_path, item_name):
    # 打开图片
    image = cv2.imread(file_path)
    # 获取图片的宽和高
    height, width, channel = image.shape
    # 计算缩放比例
    new_width = None
    new_height = None
    if width < height:
        print("720x1280: ", item_name)
        new_width = 720
        new_height = 1280
    else:
        print("1280x720: ", item_name)
        new_width = 1280
        new_height = 720
    # 缩放图片
    # image = image.resize((new_width, new_height), Image.ANTIALIAS)
    image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    # 保存图片
    # image.save(result_path)
    cv2.imwrite(result_path, image)

# 测试
process_files('.\\data')
