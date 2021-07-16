from linkedlist import takeinput, printdata

def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count

head=takeinput()
printdata(head)
print(length(head))
