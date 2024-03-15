#Simple calculator program

def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def division(n1, n2):
    return n1/n2


num1, num2 = map(int,input("Enter the num1 and num2: ").split(" "))

choice = input("Type 1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")

if choice == "1":
    res = add(num1, num2)
elif choice == "2":
    res = sub(num1, num2)
elif choice == "3":
    res = multiply(num1, num2)
elif choice == "4":
    res = division(num1, num2)

print(res)