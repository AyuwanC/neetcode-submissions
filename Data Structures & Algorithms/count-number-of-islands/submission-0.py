class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        numrows = len(grid)
        numcols = len(grid[0])
        visited = set()
        def dfs(row, col):
            nonlocal grid, visited
            if not 0<=row<numrows or not 0<=col<numcols:
                return False
            if grid[row][col] == '0':
                return False
            if (row, col) in visited:
                return False
            visited.add((row, col))
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
            # up = grid[row-1][col]
            # down = grid[row+1][col]
            # left = grid[row][col-1]
            # right = grid[row][col+1]
        for x in range(numrows):
            for y in range(numcols):
                if grid[x][y] == '1' and (x, y) not in visited:
                    dfs(x, y)
                    ans += 1
        return ans

                    