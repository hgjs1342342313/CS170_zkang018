import ForwardSelection as fs
import BackwardElimination as be
import random
import NN
import numpy as np
import RDM as rdm
# Generate a random feature array
# 此时的feature array是一个随机生成的数组，后面可以改成从文件中读取
# 每一个feature是一个概率， 表示这个feature的结果
# 使用独立概率，score = feature1 * feature2 * feature3 * feature4 * feature5...

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
    # print("Please enter total number of features:")
    # total_features = int(input())
    # randomFeature = feature(total_features)
    print("Please input 1 to select Large dataset, 2 to select Small dataset")
    dataset = int(input())
    if dataset == 1:
        #fileaddress = "CS170_Spring_2022_Large_data__38.txt"
        fileaddress = "CS170_Spring_2022_Large_data__38.txt"
    else:
        #fileaddress = "CS170_Spring_2022_Small_data__38.txt"
        fileaddress = "CS170_Spring_2022_Small_data__38.txt"
    print("Type the number of algorithm you want to run:")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    print("3. Zheming's randomly return the answer function")
    algorithm = int(input())
    print("Beginning search")
    NN.wash_data(fileaddress)
    data = np.loadtxt('cleaned_file.txt', delimiter="  ", dtype= 'str')  
    if algorithm == 1:
        # Forward Selection
        # initState = state()
        fs.ForwardSelection(data)
    elif algorithm == 2:
        # Backward Elimination
        # initState = state(randomFeature)
        be.BackwardElimination(data)
    elif algorithm == 3:
        rdm.randomlyReturn(data)
    else:
        print("Invalid input")
