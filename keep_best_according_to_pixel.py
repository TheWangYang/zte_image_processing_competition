from PIL import Image
import os

# 定义目标长宽
RESULTS_PATH = ".\\results\\2023050704"

# 遍历目录下的所有文件
def process_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        if files == []: continue
        print("files: ", files)
        # 按照分辨率最高的图像进行复制
        item_name = subdir.split('\\')[-1]
        result_path = RESULTS_PATH + "\\" + item_name
        os.makedirs(result_path, exist_ok=True)
        result_path_list = []
        # 得到原始图片中最大分辨率的路径
        max_pixel_image_path = ""
        MAX_PIXEL = 0

        # 遍历所有的图片得到最高分辨率的进行缩放
        for file in files:
            new_result_path = result_path + "\\" + file
            print("new result_path: ", new_result_path)
            result_path_list.append(new_result_path)

            # 判断文件是否为图片格式
            if file.endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
                # 获取文件的完整路径
                file_path = os.path.join(subdir, file)
                image = Image.open(file_path)
                width, height = image.size
                pixel = height * width
                if pixel > MAX_PIXEL:
                    MAX_PIXEL = pixel
                    max_pixel_image_path = file_path
        print("max_pixel_image_path: ", max_pixel_image_path)
        # 批量处理图片
        process_image(max_pixel_image_path, result_path_list)

# 处理多张图片
def process_image(max_pixel_image_path, result_path_list):
    # 打开图片
    image = Image.open(max_pixel_image_path)
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
process_files('.\\data')



