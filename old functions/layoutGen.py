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

#I need to run this more than the number of nodes I want to get the number of nodes I want. 
#gg = layoutGen(spaceMin, 11, 250)
#len( gg.keys() )