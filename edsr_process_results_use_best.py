from PIL import Image
import os

# 定义目标长宽
RESULTS_PATH = ".\\results\\2023050805"

# 遍历目录下的所有文件
def process_files(src_dir, root_dir):
    src_list = []
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
            # 批量处理图片
            process_image(src_list[index], result_path_list)
        
        index = index + 1

# 处理多张图片
def process_image(src_path, result_path_list):
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
    image = image.resize((new_width, new_height), Image.BICUBIC)
    
    for path in result_path_list:
        # 保存图片
        image.save(path)

# 测试
process_files('.\\results-Demo', '.\\need_process_data\\data')



