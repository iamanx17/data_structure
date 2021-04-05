from Node import *

def printati(head,i):
    count=0
    while count<i:
        head=head.next
        count+=1
    return head.data

for i in range(int(input())):
    head=takeinput()
    pos=int(input())
    print(printati(head,pos))