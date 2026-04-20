class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        return node
    
    def insert(self, node):
        #assign the node connections and the tail connections
        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node #forward pointer fixed too
        self.tail.prev = node #(makes the prev pointer correct)



    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.remove(self.cache[key])
            self.insert(node)
            return self.cache[key].value

        return -1
   

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            _ = self.remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            _ = self.remove(lru)
            del self.cache[lru.key]
        



        
