# Daily Challenge 22-04-2022
# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.hs = [-1 for i in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.hs[key] = value

    def get(self, key: int) -> int:
        return self.hs[key]

    def remove(self, key: int) -> None:
        self.hs[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)