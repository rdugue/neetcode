class MyHashMap:

    def __init__(self):
        self.mod = 10 ** 4
        self.map = [-1 for _ in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        self.map[key % self.mod] = value 

    def get(self, key: int) -> int:
        return self.map[key % self.mod]

    def remove(self, key: int) -> None:
        self.map[key % self.mod] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)