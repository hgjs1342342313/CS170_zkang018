import numpy as np
import random
def cross_val_score(data, current_set, feature_to_add):
    return random.random()

def ForwardSelection(data, datalength):
    """
    Forward Selection
    :param data: features array
    :return: selected features
    """
    print("Beginning Forward Selection")
    current_set = [] #当前的feature set
    global_best_score = 0.0
    for i in range(len(data)):
        print("Considering the ", i+1, "th feature")
        print("")
        feature_to_add = -1
        best_new_score = 0.0

        for j in data:
            if j in current_set:
                continue
            accuracy = cross_val_score(data, current_set, j)
            current_set.append(j)
            print("Using feature(s) ", current_set, " accuracy is ", accuracy)
            current_set.remove(j)
            print("")
            if accuracy > best_new_score:
                feature_to_add = j
                best_new_score = accuracy
        if best_new_score >= global_best_score:
            global_best_score = best_new_score
        else:
            print("(Warning, Accuracy has decreased!)")
        current_set.append(feature_to_add)
        print("Feature set ", current_set, " was best, accuracy is ", best_new_score)
        #print("Adding feature ", feature_to_add, " to the current set")