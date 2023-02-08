import DataStructure as ds
import numpy as np

def AStar_ND(initial_arr ,goal_arr):
    open = [initial_arr]
    close = []
 
    while len(open) > 0:   #OPEN表是否为空表
        open_1 = [i.state for i in open]    #访问open节点内的state
        close_1 = [i.state for i in close]
 
        n = open.pop(0)     #删除OPEN队头节点（此点排序后为最小距离和），并且赋值给n
        close.append(n)     #n注入CLOSE表
            
        if n.state == goal_arr:
            print('最优路径如下：')
            print(np.array(n.state))    #转换成矩阵打印最终节点
            ds.print_path(n)
            break
        else:
            for i in n.get_children():  #添加子节点进OPEN
                if i.state not in open_1:
                    if i.state not in close_1:
                        open.insert(0,i)
                        open.sort(key = lambda x: x.nd_nums + x.cost)  #按不在位数＋cost 进行排序
 
    ds.print_line()
    ds.search_line(close)
    print('搜索步骤为',len(close) - 1)

def AStar_MHT(initial_arr,goal_arr):
    open = [initial_arr]
    close = []
 
    while len(open) > 0:   #OPEN表是否为空表
        open_1 = [i.state for i in open]    #访问open节点内的state
        close_1 = [i.state for i in close]
 
        n = open.pop(0)     #删除OPEN队头节点（此点排序后为最小距离和），并且赋值给n
        close.append(n)     #n注入CLOSE表
            
        if n.state == goal_arr:
            print('最优路径如下：')
            print(np.array(n.state))    #转换成矩阵打印最终节点
            ds.print_path(n)
            break
        else:
            for i in n.get_children():  #添加子节点进OPEN
                if i.state not in open_1:
                    if i.state not in close_1:
                        open.insert(0,i)
                        open.sort(key = lambda x: x.distance + x.cost)  #按曼哈顿距离＋cost 进行排序
 
    ds.print_line()
    ds.search_line(close)
    print('搜索步骤为',len(close) - 1,'总估价为',close[-1].cost+close[-1].distance)

def UCS(initial_arr,goal_arr):
    open = [initial_arr]
    close = []
 
    while len(open) > 0:   #OPEN表是否为空表
        open_3 = [i.state for i in open]    #访问open节点内的state
        close_3 = [i.state for i in close]
 
        open_4 = [i.cost for i in open]   #OPEN内每个节点的cost
        min_index = open_4.index(min(open_4))
 
        n = open.pop(min_index)     #删除OPEN队头节点，并且赋值给n
        close.append(n)     #n注入CLOSE表
            
        if n.state == goal_arr:
            print('最优路径如下：')
            print(np.array(n.state))    #转换成矩阵打印最终节点
            ds.print_path(n)
            break
        else:
            for i in n.get_children():  #添加子节点进OPEN
                if i.state not in open_3:
                    if i.state not in close_3:
                        open.append(i)
 
    ds.print_line()
    ds.search_line(close)
    print('搜索步骤为',len(close) - 1, '权重为',close[-1].cost)

def main() :
    print("press 1 to input your initial state, press 2 to use default state")
    i = int(input())
    initial = "123 450 786"
    if i == 1:
        print("please input your state. The format should be like \"123 456 780\", where 0 is the blank")
        initial = input()
    elif i == 2:
        pass
    else:
        print("invalid input, close!")
        return
    goal = "123 456 780"
    
    if ds.solutionAvail(initial, goal):
        goal_arr = ds.input_state(goal)
        initial_arr = ds.state(ds.input_state(initial), 
        parent=None,
        depth=0,
        cost=0,
        distance=ds.manhattan(ds.input_state(initial), goal_arr),
        mis_nums=ds.not_digits(ds.input_state(initial), goal_arr)
        )
        print("Now, print 1 to use UCS, print 2 to use A star with misplaced tiles, print 3 to use A star with distance")
        i = int(input())
        if i ==1:
            UCS(initial_arr, goal_arr)
        elif i == 2:
            AStar_ND(initial_arr, goal_arr)
        elif i == 3:
            AStar_MHT(initial_arr, goal_arr)
        else:
            print("invalid input. Shut down!")
            return 
    else:
        print("The state could not be solved!")
    

if __name__ == '__main__':
    main()
