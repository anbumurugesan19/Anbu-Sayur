#input : (a) (a (b()))
#output: balanced
#input: a)()
#output: unbalanced
open = ["(","[","{"]
close = [")","]","}"]
def isBalance(str):
    stack = [] # {[()]}
    for char in str:
        if char in open:
            stack.append(char)
        elif char in close:
            position = close.index(char)
            if (len(stack) > 0) and (open[position] == stack[len(stack)-1]):
                stack.pop()
            else:
                return stack
    return stack
       
str = input()
res = isBalance(str)
if len(res) == 0:
    print("Balanced")
else:
     print("UnBalanced")



    


