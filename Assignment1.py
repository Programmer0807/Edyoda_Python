
n = 0
n1 = 1
count = 0
print(n,n1,end=' ')
for i in range(8):
    i = n + n1
    n = n1
    n1 = i
    count += 1
    print(i,end=' ')