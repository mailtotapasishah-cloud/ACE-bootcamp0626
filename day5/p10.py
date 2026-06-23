with open("/workspaces/ACE-bootcamp0626/day5/p7.py", "rb") as f:
   content = f.read(2000)
with open("/workspaces/ACE-bootcamp0626/day5/p7.py", "wb") as cf:
      while content>0:
       cf.write(content)
       content = f.read(2000)