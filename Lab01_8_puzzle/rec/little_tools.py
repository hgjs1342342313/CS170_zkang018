import numpy as np
#print path
def print_path(n):
    if n.parent == None:
        return
    else:
        print("^")
        print(np.array(n.parent.state))
        print_path(n.parent)

#print divide lines
def print_line():
    print("-`-`-`-" * 5)
    print("`-`-`-`" * 5)

#print searching line
def search_line(close):
    print("search line:")
    for i in close[:-1]:
        print(np.array(i.state))
        print("v")
    print(np.array(close[-1].state))

# A* weight for euclidean distance
def AEucli(item):
    return item.cost + item.distance

# A* weight for misplaced tiles
def AMisplaced(item):
    return item.cost + item.mis_nums

