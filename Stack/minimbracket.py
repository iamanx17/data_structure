from stack import Stack


def minimbracketreversal(string, s):
    for i in string:
        if i in '{':
            s.push(i)
        
        if i == '}':
            s.pop()
    
    if s.size()%2==0:
        return int(s.size()/2)
    else:
        return -1


s=Stack()    
string=input()
print(minimbracketreversal(string,s))