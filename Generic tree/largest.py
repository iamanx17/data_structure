from GenericTree import takeinput, prindata


def largestdata(root):
    if root is None:
        return 0
    lrg=root.data
    for child in root.children:
        if child.data>lrg:
            lrg=child.data
        maxchild=largestdata(child)
        if maxchild>lrg:
            lrg=maxchild
        
    return lrg


root=takeinput()
prindata(root)