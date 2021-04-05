from Node import *

def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count


for i in range(int(input())):
    head=takeinput()
    print(length(head))