fname= input("Enter a file name you want to open"
f=open("/workspaces/ACE-bootcamp0626/day5/p7.py","w")
if(f):
f.write("I Liking working with codes")
print("File Name is",f.name)
print(f.tell())
f.close()
print(f.closed)
try:
    with open("/workspaces/ACE-bootcamp0626/day5/p7.py","r") as f:
        print(f.read())
except Exception as e:
    print(e)
print(f.closed)