def movementTester(x, layout, possibilities):
    # x is a list representing the current position of a node. This function will test whether the four directions a node can move into are occupied
    # this outputs a true / false list where false corresponds to positions available to move into at each step
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