import A1
import A2
import UniformCostSearch as ucs
import main as Ds
import little_tools as lt
import random
from datetime import datetime

def getRandomString(str):
    stl = list(str)
    random.shuffle(stl)
    stl = ''.join(stl)
    return stl

def main():
    initialstr = "521483076"
    goalstr = "123456780"
    timearr1 = []
    timearr2 = []
    timearr3 = []
    counter = 10
    print("A-Star with Manhattan:")
    for i in range(counter):
        initial = getRandomString(initialstr)
        goal = goalstr
        if Ds.solutionAvail(initial, goal):
            goalarr = Ds.input_state(goal)
            initialarr = Ds.state(Ds.input_state(initial), 
                parent = None,
                depth = 0,
                cost = 0,
                distance = Ds.manhattan(Ds.input_state(initial), goalarr),
                mis_nums = Ds.not_digits(Ds.input_state(initial), goalarr)
            )
            startime = datetime.now()
            A2.AStar_Manhattan(initialarr, goalarr)
            endtime = datetime.now()
            print(i, " times searching ends. Time is ", endtime - startime)
            timearr1.append(endtime-startime)
        else:
            print(i, " times attempt is un-solvable!")


    print("A-Star with Misplaced Tiles")            
    for i in range(counter):
        initial = getRandomString(initialstr)
        goal = goalstr
        if Ds.solutionAvail(initial, goal):
            goalarr = Ds.input_state(goal)
            initialarr = Ds.state(Ds.input_state(initial), 
                parent = None,
                depth = 0,
                cost = 0,
                distance = Ds.manhattan(Ds.input_state(initial), goalarr),
                mis_nums = Ds.not_digits(Ds.input_state(initial), goalarr)
            )
            startime = datetime.now()
            A1.AStar_Misplaced(initialarr, goalarr)
            endtime = datetime.now()
            print(i, " times searching ends. Time is ", endtime - startime)
            timearr2.append(endtime-startime)
        else:
            print(i, " times attempt is un-solvable!")

    print("UCS")
    for i in range(counter):
        initial = getRandomString(initialstr)
        goal = goalstr
        if Ds.solutionAvail(initial, goal):
            goalarr = Ds.input_state(goal)
            initialarr = Ds.state(Ds.input_state(initial), 
                parent = None,
                depth = 0,
                cost = 0,
                distance = Ds.manhattan(Ds.input_state(initial), goalarr),
                mis_nums = Ds.not_digits(Ds.input_state(initial), goalarr)
            )
            startime = datetime.now()
            ucs.UCS(initialarr, goalarr)
            endtime = datetime.now()
            print(i, " times searching ends. Time is ", endtime - startime)
            timearr3.append(endtime-startime)
        else:
            print(i, " times attempt is un-solvable!")




if __name__ == '__main__':
    main()