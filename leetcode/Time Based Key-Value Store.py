# Daily Challenge 06-10-2022
# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
		# Set value to dictionary => [Key: [Timestamp: Value]]
        if key in self.dict:
            self.dict[key][timestamp] = value
        else:
            self.dict[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
		# Get value from timestamp from the dictionary if not found -1 until found the value
        if key in self.dict:
            for i in reversed(range(1, timestamp + 1)):
                if i in self.dict[key]:
                    return self.dict[key][i]
        
        return ""