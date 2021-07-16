from stack import Stack

def balanced(string,s):
    for i in string:
        if i in '{[(':
            s.push(i)
        elif s.top()=='(' and i==')':
            s.pop()
        elif s.top()=='{' and i=='}':
            s.pop()
        elif s.top()=='[' and i==']':
            s.pop() 
    
    if s.isEmpty():
        return True
    else:
        return False


string=input()
s=Stack()
print(balanced(string, s))