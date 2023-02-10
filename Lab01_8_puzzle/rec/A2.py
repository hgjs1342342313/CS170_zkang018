import little_tools as lt
import numpy as np
#A-star, manhanttan
# Refactorying!
# def AStar_Euclidean(initial_arr, goal_arr)

# [arr means array]Parameters: initial_array: the initial state; goal_array: the goal state
# variables: open: The new nodes that we need to explore
#            close: The nodes that we have explored
#
def AStar_Euclidean(initial_arr, goal_arr):
    open = [initial_arr]
    close = []
    kkk = 0
    max_open = 0
    while len(open):
        sub_open = [i.state for i in open]
        sub_close = [i.state for i in close]
        print("times: ", kkk)
        
        if kkk > 1e6:
            break
        open.sort(key = lt.AEucli)
        max_open = max(max_open, len(open))
        head = open.pop(0)
        close.append(head)
        kkk += 1
        if head.state == goal_arr:
            print("Find optimial solution by A-Star Euclidean!")
            print("The path is: ")
            print(np.array(head.state))
            lt.print_path(head)
            break
        else:
            print("The best state to expand with g(n) = ", head.cost, " and h(n) = ", head.distance, " h(n) + g(n) = ", head.cost + head.distance," is...")
            print(np.array(head.state), "Expanding this node...")
            print("\n")
            childs = head.get_children()
            for i in childs:
                if (i.state not in sub_close) and (i.state not in sub_open):
                    open.append(i)
            

                        
    lt.print_line()
    print("\n To solve this problem the search algorithm expanded a total of ", len(close), " nodes.")
    print("The maximum number of nodes in the queue at any one time was ", max_open)
    print("The depth of the goal node was ", close[-1].depth)