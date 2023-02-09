import little_tools as lt
import numpy as np

#UCS
def getMinIndex(arr):
    return arr.index(min(arr))
#def ucs(initial_arr, goal_arr)
def ucs(initial_arr, goal_arr):
    open = [initial_arr]
    close = []
    while len(open):
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
            for i in head.get_children():
                if i.state not in sub_open:
                    if i.state not in sub_close:
                        open.append(i)
    lt.print_line()
    lt.search_line(close)
    print("Searching length is ", len(close)-1, "Weight of the final node is ", close[-1].cost)
