class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        arr = [0 for _ in range(target + 1)]
        for i in range(n):
            arr[position[i]] = speed[i]
        stack = []
        time = 0
        for i in range(target, -1, -1):
            if arr[i]:
                time1 = (target - i) / arr[i]
                if time1 > time:
                    stack.append(time1)
                    time = time1
        return len(stack)