from Node import *

def delete(head,i):
    count=0
    source=head
    while count<i:
        curr=source
        source=source.next
        count+=1
    curr.next=source.next
    return head

for i in range(int(input())):
    head=takeinput()
    pos=int(input())
    printdata(delete(head,pos))