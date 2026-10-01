class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n - 1
        while i != j:
            num1, num2 = numbers[i], numbers[j]
            if num1 + num2 < target:
                i += 1
                continue
            elif num1 + num2 > target:
                j -= 1
                continue
            else:
                return [i+1, j+1]