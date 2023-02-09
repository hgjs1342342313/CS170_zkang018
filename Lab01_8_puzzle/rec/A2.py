import little_tools as lt
import numpy as np
#A-star, manhanttan
# Refactorying!
# def AStar_Manhattan(initial_arr, goal_arr)

# [arr means array]Parameters: initial_array: the initial state; goal_array: the goal state
# variables: open: The new nodes that we need to explore
#            close: The nodes that we have explored
#
def AStar_Manhattan(initial_arr, goal_arr):
    open = [initial_arr]
    close = []
    kkk = 0
    while len(open):
        print("times: ", kkk)
        kkk += 1
        if kkk > 1e6:
            break
        head = open.pop(0)
        close.append(head)
        open.sort(key = lt.AManha)
        if head.state == goal_arr:
            print("Find optimial solution by A-Star Manhattan!")
            print("The path is: ")
            print(np.array(head.state))
            lt.print_path(head)
            break
        else:
            print("The best state to expand with g(n) = ", head.cost, " and h(n) = ", head.distance, " is...")
            print(np.array(head.state), "Expanding this node...")
            for i in head.get_children():
                if i.state not in close:
                    if i.state not in open:
                        open.append(i)
                        
    lt.print_line()
    lt.search_line(close)
    print("Totally length of path is", len(close)-1, "Final cost is: ", close[-1].cost+close[-1].distance)
    lt.print_line()
    lt.search_line(close)
    print("Totally length of path is", len(close)-1, "Final cost is: ", close[-1].cost+close[-1].distance)


