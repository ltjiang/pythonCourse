def function1():
    print("My python function!")
    return "Good"

def addfunction(a,b):
    return a+b

def printname(score = 100, s = "NoName"):
    print("Name is %s score is %d" % (s,score))
    return

s2=function1() * 2
print("%s"%s2)
c=addfunction(5,9)
print("the sum is %d" %c)
name = "Xiyun Song"
printname()