class Solution(object):
    def isUnique(self, grid, x, y):
        unique_nums = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                num = grid[x + i][y + j]
                if num in unique_nums or num < 1 or num > 9:
                    return False
                unique_nums.add(num)
        return True

    def checkRows(self, grid, x, y):
        rowSum = grid[x - 1][y - 1] + grid[x - 1][y] + grid[x - 1][y + 1]
        for i in range(2):
            if rowSum != grid[x - i][y - 1] + grid[x - i][y] + grid[x - i][y + 1]:
                return -1
        return rowSum

    def checkCols(self, grid, x, y):
        colSum = grid[x - 1][y - 1] + grid[x][y - 1] + grid[x + 1][y - 1]
        for i in range(2):
            if colSum != grid[x - 1][y - i] + grid[x][y - i] + grid[x + 1][y - i]:
                return -1
        return colSum

    def checkDiagonal(self, grid, x, y):
        diagonalSum = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
        if diagonalSum != grid[x + 1][y - 1] + grid[x][y] + grid[x - 1][y + 1]:
            return -1
        return diagonalSum

    def numMagicSquaresInside(self, grid):
        rowLen = len(grid[0])
        colLen = len(grid)
        result = 0
        for i in range(1, colLen - 1):
            for j in range(1, rowLen - 1):
                colSum = self.checkCols(grid, i, j)
                if self.isUnique(grid, i, j) == False or colSum == -1:
                    continue
                if (
                    colSum
                    == self.checkRows(grid, i, j)
                    == self.checkDiagonal(grid, i, j)
                ):
                    result += 1

        return result