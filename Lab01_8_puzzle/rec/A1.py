import little_tools as lt
import numpy as np

#A* misplaced tiles
# Refectorying!

# def AStar_Misplaced
# [arr means array]Parameters: initial_array: the initial state; goal_array: the goal state
# variables: open: The new nodes that we need to explore
#            close: The nodes that we have explored
#         
# 

   
def AStar_Misplaced(initial_arr, goal_arr):
    open = [initial_arr]
    close = []
    kkk = 0 # kkk is the counter
    max_open = len(open) # max_open is the maximum length of open
    # for all nodes in open,
    while len(open):
        # print("counter: ", kkk, " len, ", len(open))
        kkk += 1
        if kkk > 1e6:
            break
        open.sort(key=lt.AMisplaced)
        head = open.pop(0)
        close.append(head)
        if head.state == goal_arr:
            print("Found!")
            print(np.array(head.state))
            lt.print_path(head)
            break
        print("The best state to expand with g(n) = ", head.cost, " and h(n) = ", head.distance, " is...")
        print(np.array(head.state), "Expanding this node...")
        childs = head.get_children()
        for i in childs:
            if (i.state not in close) and (i.state not in open):
                open.append(i)
        max_open = max(max_open, len(open))
    
    lt.print_line()
    print("\n To solve this problem the search algorithm expanded a total of ", len(close), " nodes.")
    print("The maximum number of nodes in the queue at any one time was ", max_open)
    print("The depth of the goal node was ", close[-1].depth)
                    