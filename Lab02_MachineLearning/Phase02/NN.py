import numpy as np
import math
import time

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    # Leave one out cross validation
    # Delete columns that are not in the current set
    data = data[:, current_set]
    number_correctly_classified = 0
    time_start_total = time.time()
    for i in range(len(data)):
        time_start_i = time.time()
        object_to_classify = data[i,1:]
        label_object_to_classify = data[i][0][0]

        nearest_neighbor_distance = 0x3f3f3f3f
        nearest_neighbor_location = 0x3f3f3f3f
        nearest_neighbor_label = 0x3f3f3f3f

        for k in range(len(data)):
            if k != i:
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

        if int(label_object_to_classify) == int(nearest_neighbor_label):
            number_correctly_classified += 1
        time_end_i = time.time()
        time_cost_i = time_end_i - time_start_i
        print("We spend ", time_cost_i, "s on the ", i, "th object")
    accuracy = number_correctly_classified / len(data)
    print("The accuracy is ", accuracy)
    time_end_total = time.time()
    time_cost_total = time_end_total - time_start_total
    print("We spend ", time_cost_total, "s in total")

filename = 'C:\\Users\\sygra\\githubFiles\\CS170_zkang018\\Lab02_MachineLearning\\Phase02\\small-test-dataset.txt'
data = np.loadtxt(filename, delimiter='  ', dtype= 'str')   
current_set = [0, 3, 5, 7]
for i in range(len(current_set)):
    current_set[i] += 1
feature_to_add = 10            
leave_one_out_cross_validation(data, current_set, feature_to_add)