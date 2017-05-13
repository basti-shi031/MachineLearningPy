from numpy import *
import operator


def createDataSet():
    group1 = [[1, 1.1], [1, 1], [0, 0], [0, 0.1]]
    group = array(group1)
    label = ['A', 'A', 'B', 'B']
    return group, label


def classfy(inX, dataSet, labels, k):
    dataSize = dataSet.shape[0]
    print(dataSize)
    diffMat = tile(inX, (dataSize, 1)) - dataSet
    print(diffMat)
    sqDiffMat = diffMat ** 2
    print(sqDiffMat)
    # 矩阵行相加
    sqDistance = sqDiffMat.sum(axis=1)
    print(sqDistance)
    distance = sqDistance ** 0.5
    print(distance)
    sortedDistance = distance.argsort()
    print(sortedDistance)

    classType = {}
    for index in range(k):
        item_label = label[sortedDistance[index]]
        classType[item_label] = classType.get(item_label, 0) + 1
    print(classType)
    sortClassType = sorted(classType.items(), key=operator.itemgetter(1), reverse=True)
    print(sortClassType)
    return sortClassType[0][0]


group, label = createDataSet()
print(classfy([1, 1], group, label, 3))
