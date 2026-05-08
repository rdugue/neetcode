class Node:

    def __init__(self, key=-1):
        self.key = key 
        self.next = None

class MyHashSet:

    def __init__(self):
        self.mod = 10 ** 4
        self.keys = [Node() for _ in range(self.mod)]

    def add(self, key: int) -> None:
        current = self.keys[key % self.mod]
        while current.next:
            if current.next.key == key:
                return 
            current = current.next
        current.next = Node(key)

    def remove(self, key: int) -> None:
        current = self.keys[key % self.mod]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return 
            current = current.next

    def contains(self, key: int) -> bool:
        current = self.keys[key % self.mod]
        while current.next:
            if current.next.key == key:
                return True 
            current = current.next
        return False 
             


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)