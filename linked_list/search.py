from Node import *

def search(head,i):
    count=0
    res=0
    while count<i:
        if head.data==i:
            res=count
        
        head=head.next
        count+=1
    
    if res>0:
        print(res)
    else:
        print(-1)


for i in range(int(input())):
    head=takeinput()
    value=int(input())
    search(head,value)