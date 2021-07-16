from stack import Stack

def redudant(s,string):
    count=0
    for i in string:
        if i == ')':
            for j in range(s.size()-1):
                if s.top() =='(':
                    count=0
                else:
                    count+=1
                s.pop()                
        else:
            s.push(i)    

    if count==0:
        return True
    else:
        return False
        
s=Stack()
string=input()
print(redudant(s,string))