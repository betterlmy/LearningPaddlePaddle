def read(path):
    with open(path, 'r', encoding="utf-8") as f:
        context = f.read()
        f.close()
    return context


def readStopWord(stopPath):
    with open(stopPath, 'r', encoding="utf-8") as f:
        stopWords = [i.strip() for i in f.readlines()]  # strip()用于删除\n等其他元素
        f.close()
        return stopWords

pass
