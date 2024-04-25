class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self, key):
        node = self.hashMap[key]
        prev = node.prev
        next_node = node.next
        #set prev node's next pointer to be the node after
        prev.next = next_node
        #set next node's prev pointer to be the node before
        next_node.prev = prev
        del self.hashMap[key]
    
    def insert(self, key, val):
        new_node = Node(key, val)
        prev_mru = self.mru.prev

        prev_mru.next = new_node
        new_node.next = self.mru
        new_node.prev = prev_mru
        self.mru.prev = new_node
        self.hashMap[key] = new_node

    def get(self, key: int) -> int:
        if key in self.hashMap:
            val = self.hashMap[key].val
            self.remove(key)
            self.insert(key, val)
            return self.hashMap[key].val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(key)
            self.insert(key, value)
        elif self.capacity == len(self.hashMap):
            node_to_remove = self.lru.next
            self.remove(node_to_remove.key)
            self.insert(key, value)
        else:
            self.insert(key, value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)