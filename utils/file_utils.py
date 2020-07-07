import os


def list_dirs(path):
    return list_files(path, False)


def list_files(path, folder=False):
    # 得到文件夹下的所有文件名称
    files = os.listdir(path)
    file_nms = []
    # 遍历文件夹
    for file in files:
        file = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(file) and folder:
            file_nms.append(os.path.abspath(file))
        elif not os.path.isdir(file) and not folder:
            file_nms.append(os.path.abspath(file))

    return file_nms
