# 实现代码的可复用和模块化
import os
import zipfile


def get_size_type(path, sizeDict=None, typeDict=None):
    # 遍历获取当前目录下所有的文件类型和数量
    if typeDict is None:
        typeDict = {}
    if sizeDict is None:
        sizeDict = {}
    files = os.listdir(path)
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

# %%
