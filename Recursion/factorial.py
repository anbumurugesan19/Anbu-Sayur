
def fact(n):

    if n==1:
        return 1
    else:
        return n * fact(n-1)


n = int(input("Enter the number: "))
if n > 0:
    print(fact(n))
else:
    while n < 0: 
        n = int(input("Enter a positive number"))
    print(fact(n))


# 3 * fact(3-1 = 2) 
#     2 * fact(2-1 = 1)
#     return 1