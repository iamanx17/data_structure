class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeinput():
    inputlist=[int(ele) for ele in input().split()]
    head=None
    tail=None
    for currdata in inputlist:
        if currdata==-1:
            break

        newnode=Node(currdata)
        if head is None:
            head=newnode
            tail=newnode
        else:
            tail.next=newnode
            tail=newnode
    return head

def printdata(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print('None')
