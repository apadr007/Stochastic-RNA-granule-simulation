import cProfile

import random
import pandas
import numpy

import time

from operator import add

## movement function
def mover(layout, spaceMax, spaceMin):
    from operator import add
    
    for key, value in layout.items():
        possibilities = numpy.zeros(shape=(5,2))
        possibilities[0] = [1, 0]
        possibilities[1] = [-1, 0]
        possibilities[2] = [0, 1]
        possibilities[3] = [0, -1]
        oldDir = list(value)

        if any(i >= spaceMax or i <= spaceMin for i in oldDir):
            newDir = bounceBack(oldDir, spaceMax, spaceMin)
            if newDir in layout.values():
                continue
            else:
                layout[key] = newDir
        else:
            possibilities = movementTester(value, layout, possibilities)
            randomDirection = random.choice( possibilities )
            newDir = map(add, value, randomDirection)
            if newDir in layout.values():
                continue
            else:
                layout[key] = newDir            
    return layout




# maintains nodes within boundary limits of lattice
def bounceBack(newDir, spaceMax, spaceMin):
    for n,i in enumerate(newDir):
        if i <= spaceMin:
            newDir[n] = spaceMin + 1
        if i >= spaceMax:
            newDir[n] = spaceMax - 1
    return newDir


# This function will test whether the four directions a node can move into are occupied
# this outputs a true / false list where false corresponds to positions available to move into at each step
def movementTester(x, layout, possibilities):
    new_possibilities = possibilities + x

    output_direction = []
    for i in new_possibilities:
        i = list(i)
        output_direction.append( (i in layout.values()) )

    output_direction = true_to_false(output_direction)
    possibilities = possibilities[output_direction]
    if possibilities.size == 0:
        possibilities = [0, 0]
        return possibilities
    else:
        return possibilities
    
#used inside movementTester
def true_to_false(y):
    #this inverts True to False
    output = []
    for i in y:
        if i == True:
             output.append((False))
        elif i == False:
            output.append((True))       
    return output

def layoutGen(spaceMin, spaceMax, nodes):

    layout = {}
    for i in range(nodes):
        x = random.choice(range(spaceMin, spaceMax) )
        y = random.choice(range(spaceMin, spaceMax) )
        z = x,y

        if not [key for key, value in layout.iteritems() if value == z]:
            layout[i] = z
        else:
            x = random.choice(range(spaceMin, spaceMax) )
            y = random.choice(range(spaceMin, spaceMax) )
            z = x,y
            if not [key for key, value in layout.iteritems() if value == z]:
                layout[i] = z
    val = 0        
    for key in layout.keys():
        layout[val] = layout.pop(key)
        val = val + 1
            
    return layout

def loop(niter, nobj):
    spaceMax = 2000
    spaceMin = 1

    layout = layoutGen(spaceMin, spaceMax, nobj)
    
    start = time.time()
    for i in range(niter):
        mover(layout, spaceMax, spaceMin)
    end = time.time()
    print(end - start)

cProfile.run('loop(9,1000)')
cProfile.run('loop(9,2000)')
cProfile.run('loop(9,4000)')
