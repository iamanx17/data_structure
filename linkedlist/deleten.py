from linkedlist import takeinput, printdata
# delete n node after m node

def deletemn(head,m,n):
    save=head
    if n==0:
        return head
    while head is not None:
        for i in range(m):
            temp=head
            if head is None:
                return save        
            head=head.next
        if head is None:
            temp.next=None
            return save
        elif head.next==None:
            temp.next=None
            return save
        else:
            for i in range(n):
                head=head.next
            temp.next=head
    return save


head=takeinput()
printdata(head)
n=int(input())
m=int(input())
printdata(deletennode(head,n,m))