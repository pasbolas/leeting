"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, i_row, i_column):

            if grid[i_row][i_column] == "0":
                return

            grid[i_row][i_column] = "0"

            # looking upwards
            if i_row - 1 >= 0:
                dfs(grid,i_row-1,i_column)

            #looking right
            if i_column + 1 < len(grid[0]):
                dfs(grid,i_row,i_column + 1)

            # Looking down
            if i_row + 1 < len(grid):
                dfs(grid,i_row + 1,i_column)

            # Looking Left
            if i_column - 1>= 0:
                dfs(grid,i_row,i_column - 1)

        count = 0
        for i_row in range(len(grid)):
            for i_column in range(len(grid[0])):
                if grid[i_row][i_column] == "1":
                    dfs(grid, i_row, i_column)
                    count +=1

        return count