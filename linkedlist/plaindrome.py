from linkedlist import takeinput, printdata

def reverse(head):
    tail=None
    while head is not None:
        nxt=head.next
        head.next=tail
        tail=head
        head=nxt
    return tail

def plaindrome(head):
    count=0
    rehead=reverse(head)
    while head.next is not None and rehead.next is not None:
        if head.data==rehead.data:
            count+=1
        head=head.next
        rehead=rehead.next
    if count>0:
        return False
    else:
        return True
    
head=takeinput()
printdata(head)
print(plaindrome(head))