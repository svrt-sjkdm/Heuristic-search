# -*- coding: utf-8 -*-
import nodo
import time
        
"""
    Heuristic search: Best First Search
"""            
def bfsearch(N,goal):
    opnNds = []               # Open nodes list
    cldNds = []               # Closed nodes list
    path = []                 # Path of the solution
    moves = 0                 # Number of movements to solve the puzzle
    expansions = 0            # Number of node expansions 
    start_time = time.time()  # Start time of the search
    
    N.h = 0
    opnNds.append([N.h,N])
    
    while opnNds:
        current = opnNds.pop(0)                        # Pop item from queue
        cm = current[1].matrix                          
        gm = goal.matrix
        if cm == gm:
            end_time = time.time()                     # End time of the search
            # Form the path by going from
            # the goal node to the root node
            node = current
            while node[1].parent:
                path.append(node[1].matrix)
                node = node[1].parent
                moves += 1
            path.append(node[1].matrix)
            break
        else:
            # Expanssion of the valid nodes
            nsum = current[1].shiftUp()
            nsdm = current[1].shiftDown()
            nslm = current[1].shiftLeft()
            nsrm = current[1].shiftRight()
            
            if len(nsum) > 0 and nsum not in cldNds:
                nsu = nodo.node(current,nsum)          # New node creation
                nsu.h = nsu.heuristic(goal.matrix)     # Compute the heuristic
                current[1].childs.append([nsu.h,nsu])  # Append to current node's child list
                opnNds.append([nsu.h,nsu])
                
            if len(nsdm) > 0 and nsdm not in cldNds:
                nsd = nodo.node(current,nsdm)
                nsd.h = nsd.heuristic(goal.matrix)
                current[1].childs.append([nsd.h,nsd])
                opnNds.append([nsd.h,nsd])
                
            if len(nslm) > 0 and nslm not in cldNds:
                nsl = nodo.node(current,nslm)
                nsl.h = nsl.heuristic(goal.matrix)
                current[1].childs.append([nsl.h,nsl])
                opnNds.append([nsl.h,nsl])
                
            if len(nsrm) > 0 and nsrm not in cldNds:
                nsr = nodo.node(current,nsrm)
                nsr.h = nsr.heuristic(goal.matrix)
                current[1].childs.append([nsr.h,nsr])
                opnNds.append([nsr.h,nsr])
                
            opnNds = sorted(opnNds,key=lambda x: x[0]) # Sort list based on heuristic
            cldNds.append(current[1].matrix)
            expansions += 1
            
    if len(path) > 0:
        print('The puzzle was solved!')
        print('\nSolution statistics: ')
        print('\nNode expansions: ', expansions)
        print('Block movements : ', moves)
        print('Solution time: ',float(end_time-start_time),'[s]\n')
        path.reverse()
    else:
        print('\nNo solution was found...')
    return path