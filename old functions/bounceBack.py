def bounceBack(newDir, spaceMax, spaceMin):
    for n,i in enumerate(newDir):
        if i <= spaceMin:
            newDir[n] = spaceMin + 1
        if i >= spaceMax:
            newDir[n] = spaceMax - 1
    return newDir