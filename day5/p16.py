xlist=[["xyz",1],["pqr",3],["klm",2],["abc",4],["abc",5],["def",4]]
print(list(sorted(xlist, key=lambda x: x[1])))
print(list(sorted(xlist, key=lambda x: x[1], reverse=True)))