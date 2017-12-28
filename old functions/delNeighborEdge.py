def delNeighborEdge(x, layout):
    x_key = [key for key, value in layout.iteritems() if value == x][0]
    
    neighborSize = g.neighbors(x_key)
    toDelete = random.choice(neighborSize)

    if toDelete >= 1:
        g.delete_edges( [(g.vs[x_key]["name"], toDelete)] )
    
    return g

