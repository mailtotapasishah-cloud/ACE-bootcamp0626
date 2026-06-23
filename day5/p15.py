from functools import reduce
slist = [1, 2, 3, 4, 5,6,7,8,9,10]
print(reduce(lambda x, y: x * y, slist))


from functools import reduce
slist = [1, 2, 3, 4, 5,6,7,8,9,10]
print(reduce(lambda x, y: x - y, slist))