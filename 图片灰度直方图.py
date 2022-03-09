import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt


def main():
    img = cv2.imread('dataSet/nezha.png', 0)
    # 得到计算灰度直方图的值
    n = np.array(img)
    xy = xygray(img)

    # 画出灰度直方图
    x_range = range(256)
    plt.plot(x_range, xy, "r", linewidth=2, c='black')
    # 设置坐标轴的范围
    y_maxValue = np.max(xy)
    plt.axis([0, 255, 0, y_maxValue])
    # 设置坐标轴的标签
    plt.xlabel('gray Level')
    plt.ylabel("number of pixels")
    plt.show()


def xygray(img):
    # 得到高和宽
    rows, cols = img.shape
    print(img.shape)
    # 存储灰度直方图
    xy = np.zeros([256], np.uint64)  # 256*1
    for r in range(rows):
        for c in range(cols):
            xy[img[r][c]] += 1
    # 返回一维ndarry
    # print(xy.sum())
    return xy


main()
