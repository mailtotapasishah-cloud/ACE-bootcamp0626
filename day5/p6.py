f=open("/workspaces/ACE-bootcamp0626/day5/p7.py","w")
f.write("a=123\nprint(a)")
print("File Name is",f.name)
print(f.tell())
f.close()
print(f.closed)
with open("/workspaces/ACE-bootcamp0626/day5/p7.py","r") as f:
    print(f.read())
print(f.closed)