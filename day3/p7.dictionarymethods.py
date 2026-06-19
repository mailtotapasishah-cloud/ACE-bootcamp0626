dic = {m for m in dir(dict) if not m.startswith('_')}
print(dic)