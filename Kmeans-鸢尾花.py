import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

# 从sklearn加载数据集
iris = datasets.load_iris()

x = iris.data
print(x.shape)
y = iris.target

# 绘制二维数据分布图
plt.scatter(x[:, 0], x[:, 1], c='red', marker='v', label='see')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend()  # legend 图例 放在位置2
plt.show()


# 封装训练器
def model(n_clusters):
    estimator = KMeans(n_clusters=n_clusters)
    return estimator


def train(estimator):
    estimator.fit(x)


estimator = model(n_clusters=3)
train(estimator)

# 可视化展示
label_predict = estimator.labels_  # 获取聚类标签
x0 = x[label_predict == 0]
x1 = x[label_predict == 1]
x2 = x[label_predict == 2]
plt.scatter(x0[:, 0], x0[:, 1], c='red', marker='o', label=iris.target_names[0])
plt.scatter(x1[:, 0], x1[:, 1], c='blue', marker='o', label=iris.target_names[1])
plt.scatter(x2[:, 0], x2[:, 1], c='yellow', marker='o', label=iris.target_names[2])
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend()
plt.show()

# 手撕kmeans
