


def sortSecond(val):
    return val[1] # val[1] means at 1st index it would sort each element of tuple in a list.
l = [(2, 5),(1, 2),(4, 4),(2, 3),(2, 1)]

l.sort(key=sortSecond)
print(l)
