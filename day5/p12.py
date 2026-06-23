slist = [1, 2, 3, 4, 5,6,7,8,9,10]
def sum_elements(a):
    m=0
    for i in range(len(a)):
        m += a[i]
    return m
result = sum_elements(slist)
print(result)

def squares(x):
    return x * x
print(list(map(lambda x: x * x, slist)))

from functools import reduce
slist = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, slist)
print(result)