import little_tools as lt
import numpy as np

#A* misplaced tiles
# Refectorying!

# def AStar_Misplaced
# [arr means array]Parameters: initial_array: the initial state; goal_array: the goal state
# variables: open: 
#            close:
#         
# 

   
def AStar_Misplaced(initial_arr, goal_arr):
    open = [initial_arr]
    close = []
    kkk = 0
    # for all nodes in open,
    while len(open):
       # print("times, ", kkk)
        print("length, ", len(open))
        kkk += 1
        sub_open = []
        sub_close = []
    # get the states of open array and close array
        for i in open:
            sub_open.append(i.state)
        for i in close:
            sub_close.append(i.state)
        head = open.pop(0)
        print("open pop! ", len(open))
        close.append(head)
        if head.state == goal_arr:
            print("A-star misplaced found!")
            print(np.array(head.state))
            lt.print_path(head)
            break
        else:
            print("New sub add")
            for i in head.get_children():
                print("i.state, ", i.state)
                if i.state not in sub_open:
                    if i.state not in sub_close:
                        open.append(i)
                        #sub_open.append(i)
                        open.sort(key=lt.AMisplaced)
    lt.print_line()
    lt.search_line(close)
    print("Searching path is", len(close) - 1)
                    