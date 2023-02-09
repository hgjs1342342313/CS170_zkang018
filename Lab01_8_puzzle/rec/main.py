#  Version 1.0: Data Structures of 8 Puzzle
#  1. State representation
#       Init_Stat: Input of Users
#       Goal_Stat: [[1 2 3], [4 5 6], [7 8 0]]
#       Operators: Move_Blank_Up, Move_Blank_Down, Move_Blank_Left, Move_Blank_Right
#  2. Class 
#       class state: The node class that represent the cost, distance, parent node
#       operators: Move blank to 4 directions: up, down, left, right
#  3. Packages:
#        numpy: the package addressing the numbers
#        random: random functions
#        copy: copy the objects
#        UniformCostSearch:
#        A1: A* misplaced tiles
#        A2: A* distance based
import numpy as np
import copy
import A1
import A2
import UniformCostSearch as ucs

import numpy as np
# Module 1: if the solution is Available
#def calcluate disordered number
def calDisNum(arrayIn):
    disNum = 0
    for i in range(1, 9):
        
        for j in range(0, i):
            if arrayIn[j]>arrayIn[i] and arrayIn[i] != '0':
                disNum += 1
    return disNum

#def if the solution is available
def solutionAvail(initialState, goalState):
    initialState = initialState.replace(" ", "")#replace space to none
    goalState = goalState.replace(" ", "")
    #disorderNumI number of disordered number in initial state
    #disorderNumG number of disordered number in goal state

    disorderNumI = calDisNum(initialState)
    disorderNumG = calDisNum(goalState)

    # judge if the Odevities of disordered number of initial state and goal state are the same 
    if(disorderNumI % 2) == (disorderNumG % 2):
        return True # available
    else:
        return False # non-available

#Module 2: get targets, children, elements that can swap, manhattan distance, misplaced tiles
#def find target
def find_target(arr, target):
    for i in arr:
        for j in i:
            if j == target:
                return arr.index(i), i.index(j)

#def swap the blank and a number, then get a child node
def get_child(arr, e):
    arr_new = copy.deepcopy(arr)
    r, c = find_target(arr_new, '0')
    r1, c1 = find_target(arr_new, e)

    arr_new[r][c], arr_new[r1][c1] = arr_new[r1][c1], arr_new[r][c]
    return arr_new

#def get all elements that can swap
def get_elements(arr):
    r, c = find_target(arr, '0')
    elements = []
    if r > 0:
        elements.append(arr[r-1][c])
    if r < 2:
        elements.append(arr[r+1][c])
    if c > 0:
        elements.append(arr[r][c-1])
    if c < 2:
        elements.append(arr[r][c+1])
    return elements

#def get manhattan distance
def manhattan(arr1, arr2):
    distance = []
    for i in arr1:
        for j in i:
            local1 = find_target(arr1, j)
            local2 = find_target(arr2, j)
            distance.append(abs(local1[0]+local2[0])+abs(local1[1]-local2[1]))
    return sum(distance)

#def get misplaced tiles number
def not_digits(arr1, arr2):
    num = 0
    for i in range(0, 2):
        for j in range(0, 2):
            if arr1[i][j] != arr2[i][j] and arr1[i][j] != 0 and arr2[i][j] != 0:
                num += 1
    
    return num

class state:
    #state: a list that represents the current state. 
    #parent: the parent node of this state
    #cost: the cost of finding this node
    #depth: the depth of the current state
    #distance: manhattan distance from this node to goal state
    #mis_nums: misplaced_tiles
    #goal_arr: goal state array
    def __init__(self, state, parent=None, depth = 1, cost = 0, distance = 0, mis_nums = 0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.distance = distance
        self.mis_nums = mis_nums
    #def get a layer of children
    def get_children(self):
        children=[]
        #get all children of this node
        for i in get_elements(self.state):
            #for each child of this node, swap them and get the child node
            child = state(state=get_child(self.state,i), 
                parent = self, 
                depth = self.depth+1, 
                cost = self.cost+1,
                distance = self.distance + manhattan(self.state, goal_arr),
                mis_nums = not_digits(self.state, goal_arr))
              
            #append the answer to the array
            children.append(child)  
        return children

#Module 4: get input
def input_state(str):
    str_list=list(str.replace(" ", ""))
    return [str_list[i:i+3] for i in range(0, len(str_list), 3)]

goal = "123 456 780"
goal_arr = input_state(goal)

def main() :
    print("press 1 to input your initial state, press 2 to use default state")
    i = int(input())
    initial = "871 602 543"
    if i == 1:
        print("please input your state. The format should be like \"123 456 780\", where 0 is the blank")
        initial = input()
    elif i == 2:
        print("using default case")
    else:
        print("invalid input, close!")
        return

    
    if solutionAvail(initial, goal):
        initial_arr = state( state = input_state(initial), 
            parent=None,
            depth=0,
            cost=0,
            distance=manhattan(input_state(initial), goal_arr),
            mis_nums=not_digits(input_state(initial), goal_arr),
        )
        print("Now, print 1 to use UCS, print 2 to use A star with misplaced tiles, print 3 to use A star with distance")
        i = int(input())
        if i ==1:
            ucs.UCS(initial_arr, goal_arr)
        elif i == 2:
            A1.AStar_Misplaced(initial_arr, goal_arr)
        elif i == 3:
            A2.AStar_Manhattan(initial_arr, goal_arr)
        else:
            print("invalid input. Shut down!")
            return 
    else:
        print("The state could not be solved!")
    

if __name__ == '__main__':
    main()
