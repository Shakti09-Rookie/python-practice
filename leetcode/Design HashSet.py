# Daily Challenge 21-04-2022
# https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.hs = [None] * self.size
        
    def calc_hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        pos = self.calc_hash(key)
        if self.hs[pos] == None:
            self.hs[pos] = [key]
        else:
            self.hs[pos].append(key)
        
    def remove(self, key: int) -> None:
        pos = self.calc_hash(key)
        if self.hs[pos] != None:
            while key in self.hs[pos]:
                self.hs[pos].remove(key)

    def contains(self, key: int) -> bool:
        pos = self.calc_hash(key)
        if self.hs[pos] != None:
            return key in self.hs[pos]
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)