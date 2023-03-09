import numpy as np
import random
import copy
import NN

def BackwardElimination(data):
    """
        Backward Elimination
        :param data: features array
        :return: selected features
    """
    print("Beginning Backward Elimination")
    current_set = [i for i in range (1, len(data[0])-1)] #当前的feature set
    global_best_score = 0.0
    global_best_set = []

    #consider the ALL feature set
    accuracy = NN.a_leave_one_out_cross_validation(data, current_set, -1)
    print("Using feature(s) ", current_set, " accuracy is ", accuracy)
    if accuracy > global_best_score:
        global_best_score = accuracy
        global_best_set = copy.deepcopy(current_set)
    

    for i in range(len(data[0])-2):
        print("Considering the ", i+1, "th feature")
        print("")
        feature_to_remove = -1
        best_new_score = 0.0

        for j in range(1, len(data[0])-1):
            if j not in current_set:
                continue
            accuracy = NN.a_leave_one_out_cross_validation(data, current_set, j)
            current_set.remove(j)
            print("Using feature(s) ", current_set, " accuracy is ", accuracy)
            current_set.append(j)
            print("")
            if accuracy > best_new_score:
                feature_to_remove = j
                best_new_score = accuracy
        if feature_to_remove != -1:
            current_set.remove(feature_to_remove)
        if best_new_score >= global_best_score:
            global_best_score = best_new_score
            global_best_set = copy.deepcopy(current_set)
        else:
            print("(Warning, Accuracy has decreased!)")
            break
        print("Feature set ", current_set, " was best, accuracy is ", best_new_score)
    print("Finished search!! The best feature subset is ", global_best_set, " , which has an accuracy of ", global_best_score)
        #print("Removing feature ", feature_to_remove, " to the current set")
