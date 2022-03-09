from wordcloud import WordCloud, ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
from imageio import imread

import jieba


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


def getPic():
    # 读入背景图片
    bg_pic = imread('图1.png')
    # 生成词云图片
    wordcloud = WordCloud(mask=bg_pic, background_color='white', \
                          scale=1.5, font_path=r'msyh.ttc').generate(' '.join(novelDict.keys()))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    # 保存图片
    wordcloud.to_file('父亲.jpg')




# print(contextList)

def analysis():
    # 读取文件
    context = read("./dataSet/词/zuowen.txt")
    stopword = readStopWord("./dataSet/词/stop.txt")

    words = list(jieba.lcut(context))
    # 创建一个字典,存放每个词,并确定每个词出现的次数
    wordDict = {}
    for word in words:
        if len(word) == 1:
            continue
        if word not in stopword:
            wordDict.setdefault(word, 0)
            wordDict[word] += 1

    # 将字典进行排序
    wordList = list(wordDict.items())
    wordList.sort(key=lambda x: x[1], reverse=True)
    wordList[:10]
    return wordList


wordList = analysis()
wordList = wordList[:10]