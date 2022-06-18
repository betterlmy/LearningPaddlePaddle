# 实现代码的可复用和模块化
import os
import zipfile


def get_size_type(path, sizeDict=None, typeDict=None):
    """遍历获取当前目录下所有的文件类型和数量(包括子目录)

    Args:
        path (string): 获取文件的路径
        sizeDict (Dict, optional): _description_. Defaults to None.
        typeDict (Dict, optional): _description_. Defaults to None.

    Returns:
        Dict: _description_
    """
    if typeDict is None:
        typeDict = {}
    if sizeDict is None:
        sizeDict = {}
    files = os.listdir(path)# 获取所有的文件和文件夹名
    for fileName in files:
        tmpPath = os.path.join(path, fileName)
        if os.path.isdir(tmpPath):
            get_size_type(tmpPath, sizeDict, typeDict)
        elif os.path.isfile(tmpPath):
            typeName = os.path.splitext(tmpPath)[1]
            if not typeName or typeName == '':
                # 如果没有后缀
                typeDict.setdefault("None", 0)  # 添加默认值
                typeDict["None"] += 1
                sizeDict.setdefault("None", 0)
                sizeDict["None"] += os.path.getsize(tmpPath)
            else:
                # 有后缀名
                typeDict.setdefault(typeName, 0)  # 添加默认值
                typeDict[typeName] += 1
                sizeDict.setdefault(typeName, 0)
                sizeDict[typeName] += os.path.getsize(tmpPath)
    return sizeDict, typeDict


def unzip_data(src_path, dest_path):
    # 解压文件
    if not os.path.isdir(dest_path):
        z = zipfile.ZipFile(src_path, 'r')
        z.extractall(path=dest_path)
        z.close()


if __name__ == '__main__':
    print(get_size_type("../"))