from PIL import Image
import os

# 定义目标文件夹位置
RESULTS_PATH = ".\\results\\2023050602\\new_results"

# 遍历目录下的所有文件
def process_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            # 判断文件是否为图片格式
            if file.endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
                # 获取文件的完整路径
                if(len(file) <= 16): continue  # 跳过当前读取直接到下一张图
                file_path = os.path.join(subdir, file)
                print("subdir: ", subdir)
                item_name = subdir.split('\\')[-1]
                result_path = RESULTS_PATH + "\\" + item_name
                os.makedirs(result_path, exist_ok=True)
                new_name = file.split("_")[0] + "_" + file.split("_")[1] + ".png"
                print("old_name: ", file)
                print("new_name: ", new_name)
                result_path = os.path.join(result_path, new_name)
                # 处理图片
                process_image(file_path, result_path, item_name)

# 处理单张图片
def process_image(file_path, result_path, item_name):
    # 打开图片
    image = Image.open(file_path)
    # 保存图片
    image.save(result_path)

# 测试
process_files('.\\results\\2023050602\\old_processing_results\\1280x720')
