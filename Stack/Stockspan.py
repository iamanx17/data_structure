from stack import Stack


def stockspan(arr,s):
    res=[]
    for i in range(len(arr)):
        if i==0:
            s.push(arr[i])
            res.append(1)
        
        if i<s.top():
            s.push(arr[i])
            res.append(1)
        else:
            while s.top()<i:
                s.pop()
            if s.isEmpty():
                res.append(i)
      
        
    return res

s=Stack()
arr=[5,3,8,7,10,7,7,12,16]
print(stockspan(arr,s))

        
