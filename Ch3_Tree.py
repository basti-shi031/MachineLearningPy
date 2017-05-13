from math import log


def calcShanonEnt(dataSet):
    data_size = len(dataSet)
    # 统计每种结果数量的字典
    data_count_dict = {}
    for data in dataSet:
        result = data[-1]
        data_count_dict[result] = data_count_dict.get(result, 0) + 1
    shannonEnt = 0
    for key in data_count_dict:
        p = float(data_count_dict.get(key)) / data_size
        shannonEnt = shannonEnt - p * log(p, 2)
    return shannonEnt


def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)

    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeature = len(dataSet[0]) - 1
    for index in range(numFeature):
        featList = [example[index] for example in dataSet]
        print(featList)


dataSet, labels = createDataSet()
print(dataSet)
# print(calcShanonEnt(dataSet))
# print(splitDataSet(dataSet, 1, 1))
print(chooseBestFeatureToSplit(dataSet))
