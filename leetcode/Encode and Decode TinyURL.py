# Daily Challenge 23-04-2022
# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    def __init__(self):
        self.h = {}
        self.c = -1
    def encode(self, longUrl: str) -> str:
        self.c+=1
        self.h[self.c] = longUrl
        return "http://tinyurl.com/" + str(self.c)

    def decode(self, shortUrl: str) -> str:
        n = len("http://tinyurl.com/")
        val = int(shortUrl[n:])
        return self.h[val]