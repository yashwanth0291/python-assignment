def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
i=int(input("enter the value :"))
result=factorial(i)
print(result)