class MyCalendar:
    
    def __init__(self):
        self.free = [[0,10**9]]


    def book(self, startTime: int, endTime: int) -> bool:
        for interval in self.free:
            if interval[0] <= startTime < endTime - 1 <= interval[1]:
                self.free.remove(interval)
                self.free.append([interval[0], startTime - 1])
                self.free.append([endTime, interval[1]])
                print(self.free)
                return True
        return False
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)