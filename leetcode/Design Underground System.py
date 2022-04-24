# Daily Challenge 24-04-2022
# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkin={}
        self.stations=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start=self.checkin[id]
        self.stations[(start[0],stationName)].append(t-start[1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = self.stations[(startStation,endStation)]
        return sum(trip)/(len(trip)*1.0)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)