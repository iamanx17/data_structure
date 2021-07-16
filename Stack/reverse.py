from stack import Stack

#move n-1 elements to s2 save last element of s1
#push n-1 elements from s2 to s1 again
#append the last element to s1


def reverse(s1, s2):
    if s1.size()<=1:
        return
    while s1.size()!=1:
        ele=s1.pop()
        s2.push(ele)
    lastelement=s1.pop()
    while s2.size()!=0:
        ele=s2.pop()
        s1.push(ele)
    
    reverse(s1,s2)
    s1.push(lastelement)

    return s1
    




s1=Stack()
s2=Stack()
for i in range(1,5):
    s1.push(i)
ans=reverse(s1,s2)
for i in range(ans.size()):
    print(ans.pop())

