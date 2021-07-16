from linkedlist import takeinput, printdata


def printati(head,i):
    count=0
    while count<i:
        head=head.next
        count+=1
    return head.data

head=takeinput()
printdata(head)
i=int(input())
print(printati(head, i))
