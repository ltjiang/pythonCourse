spam = -99
def scope_test():
    def do_local():
        spam = "local"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test"
    do_local()
    print("local %s" % spam)
    do_nonlocal()
    print("non local %s" % spam)
    do_global()
    print("global %s" % spam)

scope_test()
print(spam)