f=open("hello.txt","r")
print(f.read())
f.close()


f=open("hello.txt","a")
f.write("a new line is added to a file")
f.close()


f=open("hello.txt","r")
print(f.read())