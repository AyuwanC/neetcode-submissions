class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0 for _ in range(n)]
        for day in range(n):
            while stack and temperatures[stack[-1]] < temperatures[day]:
                prev_day = stack.pop()
                result[prev_day] = day - prev_day
            stack.append(day)
        return result
