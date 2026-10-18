class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(x: int, y: int):
            if x < 0 or x > len(grid) - 1:
                return None
            
            if y < 0 or y > len(grid[x]) - 1:
                return None
            
            if grid[x][y] == "1":
                grid[x][y] = "0"
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
            
            return None

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count


