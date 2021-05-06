#x=lambda a:a+60
#print(x(5))
def f(n):
    return lambda a:a*n
doub=f(2)
trip=f(3)
print(doub(11))
print(trip(22))