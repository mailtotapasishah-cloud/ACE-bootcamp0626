class Student:
    def __init__(self,name,branch,rollno):
        self.name=name
        self.branch=branch
        self.rollno=rollno
    def get_branch(self):
        return self.branch
    def set_branch(self, branch):
        self.branch = branch
    def del_branch(self):
        self.branch = None
s1 = Student("My","Friend",111)
s1.set_branch("CSM")
print(s1.get_branch())
s1.del_branch()
print(s1.get_branch())