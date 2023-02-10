import little_tools as lt
import numpy as np

#UCS
def getMinIndex(arr):
    return arr.index(min(arr))

#def ucs(initial_arr, goal_arr)
#Parameters: initial_array: the initial state; goal_array: the goal state
#variables: open: The new nodes that we need to explore
#           close: The nodes that we have explored
#           sub_open: The states of open array
#           sub_close: The states of close array
#           costarray: The cost of each node in open array
#           min_index: The index of the node with the minimum cost in open array
#           head: The node with the minimum cost in open array
#           i: The children of head
def UCS(initial_arr, goal_arr):
    open = [initial_arr]
    close = []
    kkk = 0
    max_open = len(open)
    while len(open):
        #print("times: ", kkk)
        kkk += 1
        if kkk > 1e6:
            break
        sub_open = []
        sub_close = []
        costarray = []
        for i in open:
            sub_open.append(i)
        for i in close:
            sub_open.append(i)
        for i in open:
            costarray.append(i.cost)
        min_index = getMinIndex(costarray)
        head = open.pop(min_index)
        close.append(head)
        if head.state==goal_arr:
            print("Find optimial path by UCS!")
            print("The path is:")
            lt.print_path(head)
            break
        else:
            print("The best state to expand with g(n) = ", head.cost, " and h(n) = ", head.distance, " is...")
            print(np.array(head.state), "Expanding this node...")
            for i in head.get_children():
                if i.state not in sub_open:
                    if i.state not in sub_close:
                        open.append(i)
            max_open = max(max_open, len(open))
    lt.print_line()
    print("\n To solve this problem the search algorithm expanded a total of ", len(close), " nodes.")
    print("The maximum number of nodes in the queue at any one time was ", max_open)
    print("The depth of the goal node was ", close[-1].depth)