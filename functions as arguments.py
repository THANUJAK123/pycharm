list=["hi","hello","how","are","u"]
def loop(x):
    print(x*4)
def trail(crazy,list):
    for i in list:
        crazy(i)
trail(loop,list)