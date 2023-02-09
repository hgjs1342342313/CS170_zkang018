import little_tools as lt
import numpy as np
#A-star, manhanttan
# Refactorying!
# def AStar_Manhattan(initial_arr, goal_arr)


def AStar_Manhattan(initial_arr, goal_arr):
    open = [initial_arr]
    close = []
    while len(open):
        sub_open = []
        sub_close = []
        for i in open:
            sub_open.append(i.state)
        for i in close:
            sub_close.append(i.state)
        
        head = open.pop(0)
        close.append(head)
        if head.state == goal_arr:
            print("Find optimial solution by A-Star Manhattan!")
            print("The path is: ")
            print(np.array(head.state))
            lt.print_path(head)
            break
        else:
            for i in head.get_children():
                if i.state not in sub_open:
                    if i.state not in sub_close:
                        open.append(i)
                        open.sort(key = lt.AManha)
    lt.print_line()
    lt.search_line(close)
    print("Totally length of path is", len(close)-1, "Final cost is: ", close[-1].cost+close[-1].distance)


