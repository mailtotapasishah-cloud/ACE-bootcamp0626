import numpy as np
arr = np.array([[1,2],[3,4]])
arr1 = np.array([[1,2],[3,4]])
arr1.flags.writeable = False #read only
marks = np.array([
    [95,100,1,55,68],
    [25,45,63,77,68]
])
print("Comparison of marks greater than 50:\n",marks[0:1],marks>45)
print(marks[0:1])
arr1[0,0] = 100
print(arr1)