from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = -1
        pathRows = [1, 0, -1, 0]
        pathCols = [0, 1, 0, -1]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for idx in range(len(pathRows)):
                    newRow, newCol = i+pathRows[idx], j+pathCols[idx]
                    if 0<=newRow<len(grid) and 0<=newCol<len(grid[0]) and grid[newRow][newCol]==1:
                        fresh -= 1
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
            time += 1
        return max(0, time) if fresh == 0 else -1