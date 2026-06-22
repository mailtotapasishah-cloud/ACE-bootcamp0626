class Student:
    def __init__(self, name, branch, rollno):
        self.Sname = name
        self.Sbranch = branch
        self.Srollno = rollno
    @classmethod
    def hike(cls):
        return "I am a class method..."

    #@classmethod
    #def hike(cls):
     #   cstart=cury - yoj
      #  match cstart:
       #     case 1:
       #            fee * cls.fee_hike
        #           break
         #   case 2 :
          #         cls.fee * cls.fee_hike)*cls.fee_hike
    def name(self):
        print(self.Sname)
    def __repr__(self):
        return f"{self.Sname},{self.Sbranch},{self.Srollno}"
    #def __str__(self):
       #return "I am str() dunder method"
S1 = Student("xyz", "ABC", 123)
S2 = Student("xyz", "ABC", 123)
S3 = Student("pqr", "RTY", 456)
print(S1.Sname, S1.Sbranch, S1.Srollno)
print(S2.Sname, S2.Sbranch, S2.Srollno)
print(S3.Sname, S3.Sbranch, S3.Srollno)
#print(S1.name())
print(S1)
print(S2)
str1="hii"
str2="hii"
print(str1)
print(str2)
print(1+2)
print(int.__add__(1,2))
print("1"+"2")
print(str.__add__("1","2"))
print(Student.hike())