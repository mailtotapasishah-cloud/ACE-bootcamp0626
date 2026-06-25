import pandas as pd
students = {
    "name": ["John","Doe", "Jane", "Smith"],
    "Rollno": [123, 456, 789, 112],
    "Branch": ["Robotics", "Computer Science", "Electrical Engineering", "Mechanical Engineering"],
    "City": ["C_ABC", "C_DEF", "C_GHI", "C_JKL"],
    "State": ["P_XYZ", "P_MNO", "P_PQR", "P_STU"]
}
df = pd.DataFrame(students)
print(df)  
print(df.shape)  
print(df["Branch"])
