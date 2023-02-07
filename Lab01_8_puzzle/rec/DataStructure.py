#  Version 1.0: Data Structures of 8 Puzzle
#  1. State representation
#       Init_Stat: Input of Users
#       Goal_Stat: [[1 2 3], [4 5 6], [7 8 0]]
#       Operators: Move_Blank_Up, Move_Blank_Down, Move_Blank_Left, Move_Blank_Right
#  2. Class 
#       class state: The node class that represent the cost, distance, parent node
#  3. Packages:
#        numpy: the package addressing the numbers
#        random: random functions
#        copy: copy the objects
#        UniformCostSearch:
#        A1: A* 
#        A2: A*
import numpy as np
import random
import copy
import UniformCostSearch
import A1
import A2

class state:
    #state: a list that represents the current state. 
    #parent: the parent node of this state
    #cost: the cost of finding this node
    #depth: the depth of the current state
    #distance: manhattan distance from this node to goal state
    #nd_nums: 
    def __init__(self, state, parent, depth, cost, distance, nd_nums):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.distance = distance
        self.nd_nums = nd_nums