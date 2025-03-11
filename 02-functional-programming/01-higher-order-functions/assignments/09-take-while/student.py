def take_while(xs, condition):
    for i in range(len(xs)):
        if condition(xs[i]) == False:
            return (xs[0:i], xs[i:])
    return (xs, [])
