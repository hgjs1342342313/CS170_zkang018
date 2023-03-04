import numpy as np
import random
def cross_val_score(data, current_set, feature_to_add):
    return random.random()

def BackwardElimination(data, datalength):
    """
        Backward Elimination
        :param data: features array
        :return: selected features
    """
    print("Beginning Backward Elimination")
    current_set = data #当前的feature set
    global_best_score = 0.0
    for i in range(len(data)):
        print("Considering the ", i+1, "th feature")
        print("")
        feature_to_remove = -1
        best_new_score = 0.0

        for j in data:
            if j not in current_set:
                continue
            accuracy = cross_val_score(data, current_set, j)
            current_set.remove(j)
            print("Using feature(s) ", current_set, " accuracy is ", accuracy)
            current_set.append(j)
            print("")
            if accuracy > best_new_score:
                feature_to_remove = j
                best_new_score = accuracy
        if best_new_score >= global_best_score:
            global_best_score = best_new_score
        else:
            print("(Warning, Accuracy has decreased!)")
        current_set.remove(feature_to_remove)
        print("Feature set ", current_set, " was best, accuracy is ", best_new_score)
        #print("Removing feature ", feature_to_remove, " to the current set")
