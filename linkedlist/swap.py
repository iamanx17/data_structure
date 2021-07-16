from linkedlist import takeinput, printdata

def swap(head,n, m):
    source=head
    curr=None
    for i in range(1,n):
        prev=head
        head=head.next
    save=head
    temp1=head.next

    for i in range(m-n):
        curr=head
        head=head.next    
    temp2=head.next

    prev.next=head
    head.next=temp1
    curr.next=save
    save.next=temp2

    return source

head=takeinput()
printdata(head)
print('Please enter value of n, m such that m>n')
n=int(input())
m=int(input())
printdata(swap(head, n, m))




    
