import numpy as np
import matplotlib as mpl
from matplotlib import colors
import matplotlib.pyplot as plt

from sklearn import svm
from sklearn import model_selection


# 加载数据集以及标签处理
# Iris数据集共150个数据,每个数据四个维度,共三种类型
def iris_type(s):
    """
    将字符串转换为整形
    :param s:
    :return:
    """
    it = {b"Iris-setosa": 0,
          b"Iris-versicolor": 1,
          b"Iris-virginica": 2}
    return it[s]


data = np.loadtxt("./dataSet/iris.data",
                  dtype=float,
                  delimiter=",",
                  converters={4: iris_type}  # 把第四列用iris_type这个函数进行转换
                  )
# print(data)

# 切分数据集
# split将特征与标签进行分割
x, y = np.split(data, (4,), axis=1)  # axis=1,对列进行处理,将前四列分割为X,剩下的分割为y
x = x[:, :2]  # 这里只用前两维进行训练

# 训练集和测试集划分,使用sklearn的model_selection
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state=1, test_size=0.2)


# 构建svm分类器
def classifier():
    clf = svm.SVC(C=.8, kernel='linear',
                  decision_function_shape='ovr')  # C 错误项的惩罚变量,越大惩罚越大,会导致过拟合,越小会导致相关性降低 decision_function_shape,一对多
    return clf


# 训练
def train(clf, x_train, y_train):
    clf.fit(x_train, y_train.ravel())


# SVM的实例化
clf = classifier()
train(clf, x_train, y_train)


# 模型准确率的定义
def show_acc(a, b, tip):
    acc = a.ravel() == b.ravel()
    print(f"{tip}的准确率是%.3f" % np.mean(acc))


# 模型的验证
def print_acc(clf, x_train, y_train, x_test, y_test):
    print("training prediction:%.3f" % (clf.score(x_train, y_train)))
    print("test prediction:%.3f" % (clf.score(x_test, y_test)))

    show_acc(clf.predict(x_train), y_train, "training data")
    show_acc(clf.predict(x_test), y_test, "training data")

    print("决策函数:", clf.decision_function(x_train)[:2])


print_acc(clf, x_train, y_train, x_test, y_test)


def draw(clf, x):
    iris_feature = 'sepal length', 'sepal width', 'petal length', 'petal width'
    # 开始画图
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()
    # 生成网格采样点
    x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]

    grid_test = np.stack((x1.flat, x2.flat), axis=1)
    print('grid_test:\n', grid_test[:2])
    # 输出样本到决策面的距离
    z = clf.decision_function(grid_test)
    print('the distance to decision plane:\n', z[:2])
    grid_hat = clf.predict(grid_test)
    # 预测分类值 得到[0, 0, ..., 2, 2]
    print('grid_hat:\n', grid_hat[:2])
    # 使得grid_hat 和 x1 形状一致
    grid_hat = grid_hat.reshape(x1.shape)
    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'b', 'r'])
    plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)  # 能够直观表现出分类边界

    plt.scatter(x[:, 0], x[:, 1], c=np.squeeze(y), edgecolor='k', s=50, cmap=cm_dark)
    plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolor='none', zorder=10)
    plt.xlabel(iris_feature[0], fontsize=20)  # 注意单词的拼写label
    plt.ylabel(iris_feature[1], fontsize=20)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.title('Iris data classification via SVM', fontsize=30)
    plt.grid()
    plt.show()


# 4 模型评估
print('-------- eval ----------')
print_acc(clf, x_train, y_train, x_test, y_test)
# 5 模型使用
print('-------- show ----------')
draw(clf, x)
