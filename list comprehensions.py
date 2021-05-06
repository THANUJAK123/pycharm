fruits=["kiwi","mango","orange","apple"]
new=[x for x in fruits if "a" in x]
print(new)
kick=[x for x in fruits if x!="mango"]
print(kick)
kick=[x.upper() for x in fruits]
print(kick)
kick=["hi" if x=="apple" else "orange" for x in fruits]
print(kick)