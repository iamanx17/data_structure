class MapNode:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=None
    

class Map:
    def __init__(self):
        self.bucketsize=10
        self.buckets=[0 for  i in range(self.bucketsize)]
        self.count=0
    

    def getbucketindex(self, hc):
        return (abs(hc)%self.bucketsize)
    
    def insert(self, key, value):
        hc=hash(key)
        index=self.getbucketindex(hc)
        head=self.buckets[index]    
        while head is not None:
            if head.key==key:
                head.value=value
                return
        head=self.buckets[index]
        newnode=MapNode(key, value)
        newnode.next=head
        self.buckets[index]=newnode
        self.count+=1
    
    def size(self):
        return self.count
    
    def getvalue(self,key):
        hc=hash(key)
        index=self.getbucketindex(hc)
        head=self.buckets[index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        return None
    
    def remove(self, key):
        hc=hash(key)
        index=self.getbucketindex(hc)
        head=self.buckets[index]
        prev=None
        while head is not None:
            if head.key==key:
                if prev is None:
                    self.buckets[index]=head
                else:
                    prev.next=head.next
                self.count-=1
                return head.value            
            prev=head
            head=head.next

        return None
    