def countX(test):
    if len(test) == 0:
        return 0
    
    if test[0] == "x":
        return 1 + countX(test[1:])

    return countX(test[1:])

print(countX("axbxcxd"))
print(countX("axbxcxdx"))

