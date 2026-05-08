class MyHashSet:

    def __init__(self):
        self.mod = 10 ** 4
        self.set = [None for _ in range(self.mod)]

    def add(self, key: int) -> None:
        self.set[key % self.mod] = key

    def remove(self, key: int) -> None:
        self.set[key % self.mod] = None

    def contains(self, key: int) -> bool:
        return self.set[key % self.mod] is not None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)