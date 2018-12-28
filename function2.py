def testarguments_int(a):
    print("before incerment id(a) = %d" % id(a))
    a += 1
    print("after incerment id(a) = %d" % id(a))
def testarguments_list(b):
    print("before incerment id(b) = %s" % id(b))
    b.append("good morning")
    print("after incerment id(b) = %d" % id(b))

num = 9
print("id(num) = %d " % id(num))
print("before call function, num = %d" % num)
testarguments_int(num)
print("id(num)=%d"% id(num))
print("after call function, num=%d" % num)

mylist = ["apple", 67]
print("id(mylist) = %d" % id(mylist))
print("before call function, mylist = %s" % mylist)
testarguments_list(mylist)
print("id(num)=%d"% id(mylist))
print("after call function, list=%s" % mylist)