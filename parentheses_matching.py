#input : (a) (a (b()))
#output: balanced
#input: a)()
#output: unbalanced
open = ["("]
close = [")"]
def isBalance(str):
    stack = []
    for char in str:
        if char in open:
            stack.append(char)
        elif char in close:
            if len(stack) == 0:
                return stack
            stack.pop()
    return stack
       
str = input()
if isBalance(str):
    print("Unbalanced")
else:
    print("Balanced")



    


