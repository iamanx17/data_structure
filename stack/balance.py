from Stack import *

stack=Stackusingll()

def balance(string):
    for i in string:
        if i in '([{':
            stack.push(i)
            stack.top()      
        elif i== ')' and stack.top()=='(':
            stack.pop()
            
        elif i==']' and stack.top()=='[':
            stack.pop()
        elif i=='}' and stack.top()=='{':
            stack.pop()
    
    
    if stack.isEmpty() is True:
        print(True)
    else:
        print(False)
        
string=input()
balance(string)


