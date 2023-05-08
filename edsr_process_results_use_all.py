from PIL import Image
import os

# 处理多个图片
def chuli_images(src_path, new_result_path):
    # 打开图片
    image = Image.open(src_path)
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
    image.save(new_result_path)



if __name__ == "main":
    RESULTS_PATH = ".\\path to results"

    # 测试
    src_dir = '.\\path to src data'
    root_dir = '.\\path to root data dir to use name list\\data'

    src_list = []

    # 对所有300张图片进行遍历得到对应的路径
    for subdir, _, files in os.walk(src_dir):
        if files == []: continue
        # 遍历所有的图片得到最高分辨率的进行缩放
        for file in files:
            src_path = src_dir + "\\" + file
            src_list.append(src_path)
    
    src_list.sort(key=lambda x : int(x.split("\\")[-1][: -14]))
    index = 0

    for subdir, _, files in os.walk(root_dir):
        print(index)
        if files == []: continue
        # 按照分辨率最高的图像进行复制
        item_name = subdir.split('\\')[-1]
        result_path = RESULTS_PATH + "\\" + item_name
        os.makedirs(result_path, exist_ok=True)

        result_path_list = []

        # 遍历所有的图片得到最高分辨率的进行缩放
        for file in files:
            new_result_path = result_path + "\\" + file
            result_path_list.append(new_result_path)
            print("new_result_path: ", new_result_path)
            # 批量处理图片
            chuli_images(src_list[index], new_result_path)
            index = index + 1



