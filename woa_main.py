# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:08:28 2020

@author: Administrator
"""
import numpy as np
import math

def fitness(sset):
    return np.sum(sset**2)


# 鲸鱼优化算法的python实现
def woa(noclus,max_iterations,noposs):
    
    ''' 
        noclus = 维度
        max_iterations = 迭代次数
        noposs = 10 # 种群数
    '''
    randomcount=0

    ground=[-10,10]
    poss_sols = np.zeros((noposs, noclus)) # whale positions
    gbest = np.zeros((noclus,)) # globally best whale postitions
    b = 2.0
    # 种群初始化
    for i in range(noposs):
        for j in range(noclus):
            poss_sols[i][j] =(ground[1]-ground[0])*np.random.rand()+ground[0]

    global_fitness = np.inf
    
    for i in range(noposs):
        cur_par_fitness = fitness(poss_sols[i])
        if cur_par_fitness < global_fitness:
            global_fitness = cur_par_fitness
            gbest = poss_sols[i]
    # 开始迭代
    trace=[]
    for it in range(max_iterations):
        for i in range(noposs):
            a = 2.0 - (2.0*it)/(1.0 * max_iterations)
            r = np.random.random_sample()
            A = 2.0*a*r - a
            C = 2.0*r
            l = 2.0 * np.random.random_sample() - 1.0
            p = np.random.random_sample()
            
            for j in range(noclus):
                x = poss_sols[i][j]
                if p < 0.5:
                    if abs(A) < 1:
                        _x = gbest[j]
                    else :
                        rand = np.random.randint(noposs)
                        _x = poss_sols[rand][j]

                    D = abs(C*_x - x)
                    updatedx = _x - A*D
                else :
                    _x = gbest[j]
                    D = abs(_x - x)
                    updatedx = D * math.exp(b*l) * math.cos(2.0* math.acos(-1.0) * l) + _x

                if updatedx < ground[0] or updatedx > ground[1]:
                    updatedx = (ground[1]-ground[0])*np.random.rand()+ground[0]
                    randomcount += 1

                poss_sols[i][j] = updatedx

            fitnessi = fitness(poss_sols[i])
            if fitnessi < global_fitness :
                global_fitness = fitnessi
                gbest = poss_sols[i]
        trace.append(global_fitness)
        print ("iteration",it,"=",global_fitness)
                
    return gbest, global_fitness,trace
# In[]
import matplotlib.pyplot as plt
gbest, fitnessi,trace=woa(5,100,10)
plt.figure()
plt.plot(np.array(trace))
plt.show()




