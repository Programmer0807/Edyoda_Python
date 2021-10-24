l = [1,2,3,4,5,6,7]
l2 = []

def tripple(value):
    result = value*3
    return result

num = list(map(tripple,l))
l.append(l2)
print(num)    