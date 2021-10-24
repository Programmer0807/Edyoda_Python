l = [4,5,2,9]
l2 = []
def square(value):
    result = value**2
    return result


v = list(map(square,l))
l.append(l2)
print(v)