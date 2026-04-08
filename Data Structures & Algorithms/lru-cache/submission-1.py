class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

        self.prev, self.next = None, None #this gives us a doubly linked list. 

#since everything has to be O(1) lets use a linked list.
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #this just maps everything. key to node. 
        self.capacity = capacity 

        self.left, self.right = Node(0,0), Node(0,0) #uses dummy nodes.

        #left = LRU, right = mostrecent
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node): #use when we need to get ride of a node.
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    #insert node at right. #it should be right before the null node.
    def insert(self,node):
        prev, nxt = self.right.prev, self.right #can do this because we saved the up in init
        prev.next = nxt.prev = node
        node.next, node.prev = nxt,prev



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #takes it out.
            self.insert(self.cache[key]) #puts it back into the far right for most recently used.
            #update most recent
            return self.cache[key].val
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) #node object made here
        self.insert(self.cache[key])    #inserted into our list.

        if len(self.cache) > self.capacity:
            #remove and delete LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
