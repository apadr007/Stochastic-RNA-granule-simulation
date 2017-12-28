def true_to_false(y):
    #this inverts True to False
    output = []
    for i in y:
        if i == True:
             output.append((False))
        elif i == False:
            output.append((True))       
    return output


