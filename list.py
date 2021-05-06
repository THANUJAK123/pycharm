thanu=["hi","hello",1,2,3,True]
print(len(thanu))
print(type(thanu))
print(thanu[0])
print(thanu[2:4])
thanu[1:4]=("how","are",5)
print(thanu)
thanu.insert(4,"amma")
print(thanu)
thanu.append("orange")
print(thanu)
thanu.remove(3)
print(thanu)
thanu.pop(1)
print(thanu)
del thanu[3]
print(thanu)
del thanu[2:4]
print(thanu)

