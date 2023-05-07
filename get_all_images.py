import os
import shutil

# 设置主目录路径和输出目录路径
main_directory = "./results/2023050501"
output_directory = "./results/need_super_pixel"

# 遍历所有子目录
for subdir in os.listdir(main_directory):
    # 获取子目录路径
    subdir_path = os.path.join(main_directory, subdir)
    # 如果子目录是一个目录而不是文件
    if os.path.isdir(subdir_path):
        # 遍历子目录中的所有文件
        for file in os.listdir(subdir_path):
            # 获取文件路径
            file_path = os.path.join(subdir_path, file)
            # 如果文件是一张图片
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                # 将文件复制到输出目录中
                shutil.copy(file_path, output_directory)
