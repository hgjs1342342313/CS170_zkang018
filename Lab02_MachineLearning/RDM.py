import numpy as np
import random
import copy
import NN

def randomlyReturn(data):
    """
    Forward Selection
    :param data: features array
    :return: selected features
    """
    print("Beginning Forward Selection")
    current_set = [] #当前的feature set
    global_best_score = 0.0
    global_best_set = []
    for i in range(len(data[0])-2):
        # if len(current_set)!=0:
        #     current_set.sort()
        print("Considering the ", i+1, "th feature")
        print("")
        feature_to_add = -1
        best_new_score = 0.0
        # print("data[0] length ", len(data[0]))
        for j in range(1, len(data[0])-1):
            print("j is ", j)
            print("current_set is ", current_set)
            if j in current_set:
                continue
            accuracy = NN.GUESS(data, current_set, j)
            current_set.append(j)
            print("Using feature(s) ", current_set, " accuracy is ", accuracy)
            current_set.remove(j)
            print("")
            if accuracy > best_new_score:
                feature_to_add = j
                best_new_score = accuracy
        
        if feature_to_add != -1:
            current_set.append(feature_to_add)
        if best_new_score >= global_best_score:
            global_best_score = best_new_score
            global_best_set = copy.deepcopy(current_set)
            print("Global set updated")
            print("The best feature subset is ", global_best_set, " , which has an accuracy of ", global_best_score)
        else:
            print("(Warning, Accuracy has decreased!)")
            break
        print("Feature set ", current_set, " was best, accuracy is ", best_new_score)
    print("Finished search!! The best feature subset is ", global_best_set, " , which has an accuracy of ", global_best_score)
        #print("Adding feature ", feature_to_add, " to the current set")