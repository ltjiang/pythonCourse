import datetime

def printmorning():
    print("good morning!")

today=datetime.datetime.today()
name="Ellen"
print("hello world!",name)
print('Today is ',today)
print('Today is ',today.strftime("%A"))
printmorning()
