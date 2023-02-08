import little_tools as lt
import numpy as np
#A*算法-曼哈顿距离
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
            lt.print_path(n)
            break
        else:
            for i in n.get_children():  #添加子节点进OPEN
                if i.state not in open_1:
                    if i.state not in close_1:
                        open.insert(0,i)
                        open.sort(key = lambda x: x.distance + x.cost)  #按曼哈顿距离＋cost 进行排序
 
    lt.print_line()
    lt.search_line(close)
    print('搜索步骤为',len(close) - 1,'总估价为',close[-1].cost+close[-1].distance)

