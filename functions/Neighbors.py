def Neighbors(x, layout):
    possibilities = numpy.zeros(shape=(4,2))
    possibilities[0] = [1, 0]
    possibilities[1] = [-1, 0]
    possibilities[2] = [0, 1]
    possibilities[3] = [0, -1]
    new_possibilities = possibilities + x

    output_direction = []
    for i in new_possibilities:
        i = list(i)
        output_direction.append( (i in layout.values()) )

    x_key = [key for key, value in layout.iteritems() if value == x][0]
    
    possibilities = possibilities[output_direction]
    randomDirection = random.choice( new_possibilities )

    for key, value in layout.iteritems():
        randomDirection = list(randomDirection)
        print value
        print randomDirection
        if value == randomDirection:
            print "Im here"
            if value != x_key:
                print "im here here"
                g.add_edge(g.vs[key]["name"], x_key)
    return g


#g = Graph(4)
#g.vs["name"] = range(4)
#layout = { 0:[2,1], 1:[3,1], 2:[2,2], 3:[2,3] }
#Neighbors([2,2], layout)
#print ''
#print ''
#print g