# -*- coding: utf-8 -*-
import bfsearch as bfs
import nodo
import numpy as np

def randMatrix():
    m = []
    l = np.arange(16)
    l = np.random.permutation(l)
    m.append(list(l[0:4]))
    m.append(list(l[4:8]))
    m.append(list(l[8:12]))
    m.append(list(l[12:16]))
    return m

def printM(m):
    for r in m:
        print(r)
    print('\n')

#initialState = nodo.node(None,[[1, 2, 6, 3],[4, 9, 5, 7], [8, 13, 11, 15],[12, 14, 10, 0]])
#finalState = nodo.node(None,[[0, 1, 2, 3],[4, 5, 6, 7], [8, 9, 10, 11],[12, 13, 14, 15]])
ist = randMatrix()    
fst = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,0]]
       
print('Initial state:')
printM(ist)
print('Goal state:')
printM(fst)

initialState = nodo.node(None,ist)
finalState = nodo.node(None,fst)

# Try to solve puzzle using Best First Search
path = bfs.bfsearch(initialState,finalState)

# Print path to the file
if len(path) > 0:
    with open('solution.txt','w') as file:
        for matrix in path:
            for row in matrix:
                file.write(str(row))
                file.write('\n')
            file.write('\n')