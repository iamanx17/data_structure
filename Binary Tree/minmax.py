from binarytree import takeinput, printdata

def minmax(root):
    if root == None:
        return 2147483647, -2147483648

    leftmin, leftmax = minmax(root.left)
    rightmin, rightmax = minmax(root.right)
    minimum = min(leftmin, rightmin, root.data)
    maximum = max(leftmax, rightmax, root.data)

    return minimum, maximum

root=takeinput()
printdata(root)
mini,maxi=minmax(root)
print(mini, maxi)
