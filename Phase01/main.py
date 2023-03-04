import ForwardSelection as fs
import BackwardElimination as be
import random

# Generate a random feature array
# 此时的feature array是一个随机生成的数组，后面可以改成从文件中读取
# 每一个feature是一个概率， 表示这个feature的结果
# 使用独立概率，score = feature1 * feature2 * feature3 * feature4 * feature5...
def feature(total_features):
    #randomly return a fte array
    fte = [i+1 for i in range(total_features)]
    return fte

# class state:
#     def __init__(self, feature):
#         self.feature = feature
#         self.score = 1
#         for i in range(len(feature)):
#             self.score *= feature[i]
    
#     def AddFeature(self, feature):
#         self.feature.append(feature)
    
#     def RemoveFeature(self, feature):
#         self.feature.remove(feature)
    


if __name__ == "__main__":
    print("Welcome to Zheming Kang's Feature Selection Agorithm")
    print("Please enter total number of features:")
    total_features = int(input())
    randomFeature = feature(total_features)
    print("Type the number of algorithm you want to run:")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    algorithm = int(input())
    print("Beginning search")
    if algorithm == 1:
        # Forward Selection
        # initState = state()
        fs.ForwardSelection(randomFeature, total_features)
    elif algorithm == 2:
        # Backward Elimination
        # initState = state(randomFeature)
        be.BackwardElimination(randomFeature, total_features)
    else:
        print("Invalid input")
