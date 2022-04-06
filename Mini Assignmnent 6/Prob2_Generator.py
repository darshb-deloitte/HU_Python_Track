def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


n = int(input("Enter the Limit:"))
x = fib(n)
for i in x:
    print(i, end=',')
