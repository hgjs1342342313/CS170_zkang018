import numpy as np
import math
import time
import random
import copy as cp

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    # Leave one out cross validation
    # Delete columns that are not in the current set
    cpset = cp.deepcopy(current_set)
    for i in range(len(cpset)):
        cpset[i] += 1
    if feature_to_add != -1:
        cpset.append(feature_to_add+1)
    cpset.append(1)
    cpset.sort()
    data = data[:, cpset]
    number_correctly_classified = 0
    #time_start_total = time.time()
    for i in range(len(data)):
        #time_start_i = time.time()
        object_to_classify = data[i,1:]
        label_object_to_classify = data[i][0][0]

        nearest_neighbor_distance = 0x3f3f3f3f
        nearest_neighbor_location = 0x3f3f3f3f
        nearest_neighbor_label = 0x3f3f3f3f

        for k in range(len(data)):
            if k != i:
                #print(label_object_to_classify, data[i][0])
                label_object_to_classify = int(label_object_to_classify)
                distance = 0     
                for j in range(len(object_to_classify)):
                    a = float(object_to_classify[j])
                    b = float(data[k][j+1])
                    meta = (a - b)**2
                    distance += meta
                distance = math.sqrt(distance)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data[nearest_neighbor_location][0][0]
       # print("The labels are ", label_object_to_classify," ", nearest_neighbor_label," ", data[i][0])
        if int(label_object_to_classify) == int(nearest_neighbor_label):
            number_correctly_classified += 1
        # time_end_i = time.time()
        # time_cost_i = time_end_i - time_start_i
        # print("We spend ", time_cost_i, "s on the ", i, "th object")
    accuracy = number_correctly_classified / len(data)
    print("The accuracy is ", accuracy)
    # time_end_total = time.time()
    # time_cost_total = time_end_total - time_start_total
    # print("We spend ", time_cost_total, "s in total")
    return accuracy

def a_leave_one_out_cross_validation(data, current_set, feature_to_remove):
    # Leave one out cross validation
    # Delete columns that are not in the current set
    cpset = cp.deepcopy(current_set)
    for i in range(len(cpset)):
        cpset[i] += 1
    if feature_to_remove != -1:
        cpset.remove(feature_to_remove+1)
    cpset.append(1)
    cpset.sort()
    data = data[:, cpset]
    number_correctly_classified = 0
    #time_start_total = time.time()
    for i in range(len(data)):
        #time_start_i = time.time()
        object_to_classify = data[i,1:]
        label_object_to_classify = data[i][0][0]

        nearest_neighbor_distance = 0x3f3f3f3f
        nearest_neighbor_location = 0x3f3f3f3f
        nearest_neighbor_label = 0x3f3f3f3f

        for k in range(len(data)):
            if k != i:
                #print(label_object_to_classify, data[i][0])
                label_object_to_classify = int(label_object_to_classify)
                distance = 0     
                for j in range(len(object_to_classify)):
                    a = float(object_to_classify[j])
                    b = float(data[k][j+1])
                    meta = (a - b)**2
                    distance += meta
                distance = math.sqrt(distance)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data[nearest_neighbor_location][0][0]
        
        #print("The labels are ", label_object_to_classify," ", nearest_neighbor_label," ", data[i][0])
        if int(label_object_to_classify) == int(nearest_neighbor_label):
            number_correctly_classified += 1
        # time_end_i = time.time()
        # time_cost_i = time_end_i - time_start_i
        # print("We spend ", time_cost_i, "s on the ", i, "th object")
    accuracy = number_correctly_classified / len(data)
    print("The accuracy is ", accuracy)
    # time_end_total = time.time()
    # time_cost_total = time_end_total - time_start_total
    # print("We spend ", time_cost_total, "s in total")
    return accuracy

def GUESS(data, current_set, feature_to_add):
    # Leave one out cross validation
    # Delete columns that are not in the current set
    cpset = cp.deepcopy(current_set)
    for i in range(len(cpset)):
        cpset[i] += 1
    if feature_to_add != -1:
        cpset.append(feature_to_add+1)
    cpset.append(1)
    cpset.sort()
    data = data[:, cpset]
    number_correctly_classified = 0
    #time_start_total = time.time()
    for i in range(len(data)):
        #time_start_i = time.time()
        object_to_classify = data[i,1:]
        label_object_to_classify = data[i][0][0]

        nearest_neighbor_distance = 0x3f3f3f3f
        nearest_neighbor_location = 0x3f3f3f3f
        nearest_neighbor_label = random.randint(1, 2)

       # print("The labels are ", label_object_to_classify," ", nearest_neighbor_label," ", data[i][0])
        if int(label_object_to_classify) == int(nearest_neighbor_label):
            number_correctly_classified += 1
        # time_end_i = time.time()
        # time_cost_i = time_end_i - time_start_i
        # print("We spend ", time_cost_i, "s on the ", i, "th object")
    accuracy = number_correctly_classified / len(data)
    print("The accuracy is ", accuracy)
    # time_end_total = time.time()
    # time_cost_total = time_end_total - time_start_total
    # print("We spend ", time_cost_total, "s in total")
    return accuracy

def wash_data(filename):
    with open(filename, 'r') as f:
        # 读取文件中的所有内容
        file_contents = f.read()

    # 检测负号前面的空格数量
    new_file_contents = ''
    for line in file_contents.split('\n'):
        new_line = ''
        words = line.split()
        for i, word in enumerate(words):
            if word.startswith('-') and len(words[i-1]) == 1:
                new_line += ' '
            new_line += word + '  '
        if new_line != '':
            new_file_contents += '  '+new_line.rstrip() + '\n'

    with open('cleaned_file.txt', 'w') as f:
        # 将修改后的内容写回文件
        f.write(new_file_contents)

if __name__ == '__main__':
    filename = 'small-test-dataset.txt'
    wash_data(filename)
    data = np.loadtxt('cleaned_file.txt', delimiter="  ", dtype= 'str')  
    # #data = np.genfromtxt(filename, delimiter=None, dtype= 'str')
    current_set = [3, 5, 7]
    
    feature_to_add = -1            
    leave_one_out_cross_validation(data, current_set, feature_to_add)