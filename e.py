# There is bank.
a=1
rate=0.06
for n in range(13):
    print("%d year, $=%f"%(n,a))
    a *=(1+rate)
import math
#e
a=1
n=1
c=True
while c:
    a =  (1+1/n)**n
    print("%d, %f"%(n,a))
    n=n+1
    if (abs(a-math.e)<0.00001):
        break