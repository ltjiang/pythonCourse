#calculate factorial using recursive function
# give 10, result 10!
def calfactorial(n):
    product = 1
    for x in range(1, num + 1):
        product *= x
    return product

num = 10
factorial = 1
for x in range (1, num+1):
    factorial *= x
    print("%d %d" % (x,factorial))

print("%d"% factorial)


"""Now we try useing recursive function"""

def calfactorial_recursive(n):
    if (n==1):
        return 1
    else:
        return n * calfactorial_recursive (n-1)
print("{}!={}".format(num,calfactorial_recursive(num)))

calfactorial_recursive(10)