with open("/workspaces/ACE-bootcamp0626/day5/rabbit.jpg",'rb')as f:
    content=f.read()
    with open("/workspaces/ACE-bootcamp0626/day5/rabbit1.jpg","wb")as cf:
        cf.write(content)