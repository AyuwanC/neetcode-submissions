class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row1 = [1]
        row2 = [1, 1]
        ans = [row1, row2]
        prevrow = row2
        if numRows == 1:
            return [row1]
        elif numRows == 2:
            return [row1, row2]
        else:
            for i in range(3, numRows + 1):
                nextrow = [1] * i
                for j in range(len(prevrow)-1):
                    nextrow[j+1] = prevrow[j] + prevrow[j+1]
                ans.append(nextrow.copy())
                prevrow = nextrow.copy()
        return ans