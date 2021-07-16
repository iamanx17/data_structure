from linkedlist import takeinput, printdata

def search(head, data):
    count=0
    while head is not None:
        count+=1
        if head.data==data:
            return True
        head=head.next
    return False

head=takeinput()
printdata(head)

data=int(input())
print(search(head, data))
