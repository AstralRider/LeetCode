class ListNode:
  def __init__(self, key, val, next=None, prev=None):
    self.val = val
    self.key = key
    self.next = next
    self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.left = ListNode("Left", 0)
        self.right = ListNode("Right", 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    
    def remove(self, node):
      prev = node.prev
      nextNode = node.next
      prev.next = nextNode
      nextNode.prev = prev
      self.size -= 1
      
    
    def insert(self, node):
      prev = self.right.prev
      prev.next = node
      node.next = self.right
      node.prev = prev
      self.right.prev = node
      self.size += 1
      


    def get(self, key: int) -> int:
      if key in self.map:
        self.remove(self.map[key])
        self.insert(self.map[key])
        return self.map[key].val
      else:
        return -1
        

    def put(self, key: int, value: int) -> None:
      if key in self.map:
        self.remove(self.map[key])
      self.map[key] = ListNode(key, value)
      self.insert(self.map[key])
      
      if self.size > self.capacity:
        node = self.left.next
        self.remove(node)
        del self.map[node.key]
        


        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)