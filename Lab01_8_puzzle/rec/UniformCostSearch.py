import DataStructure as ds
import numpy as np

#一致代价优先搜索
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