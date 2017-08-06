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


