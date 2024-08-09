class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        result = []
        result.append([rStart, cStart])
        visitSum = 1
        direction = 0
        distance = 1
        while visitSum < rows * cols:
            for i in range(distance):
                rStart += dx[direction]
                cStart += dy[direction]
                if 0 <= rStart and rStart < rows and 0 <= cStart and cStart < cols:
                    result.append([rStart, cStart])
                    visitSum += 1
            direction = (direction + 1) % 4
            if direction % 2 == 0:
                distance += 1

        return result