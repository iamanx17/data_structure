def rotatearr(arr, n):
    temp=[]
    for i in range(n):
        temp.append(arr[0])
        del arr[0]        
    for i in temp:
        arr.append(i)    
    return arr

arr=[int(ele) for ele in input().split()]
n=int(input())
print(rotatearr(arr,n))