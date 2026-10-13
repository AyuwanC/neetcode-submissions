class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        time = 0
        for pos, spd in cars:
            time1 = (target - pos) / spd
            if time1 > time:
                fleets += 1
                time = time1
        return fleets