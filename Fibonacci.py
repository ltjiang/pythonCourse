def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)

x = 10
print("The %dth fibonacci number %d ", fibonacci(x))