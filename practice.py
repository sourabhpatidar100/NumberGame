def myfunc(a):
  return lambda a : a * 3

mytripler = myfunc(11)
print(mytripler(11))