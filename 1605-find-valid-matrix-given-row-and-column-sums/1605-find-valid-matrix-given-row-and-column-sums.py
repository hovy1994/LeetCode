class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        rowLen = len(rowSum)
        colLen = len(colSum)
        curRowSum = [0 for _ in range(rowLen)]
        curColSum = [0 for _ in range(colLen)]
        result = [[[] for _ in range(colLen)] for _ in range(rowLen)]
        for i in range(rowLen):
            for j in range(colLen):
                result[i][j] = min(rowSum[i] - curRowSum[i], colSum[j] - curColSum[j])
                curRowSum[i] += result[i][j]
                curColSum[j] += result[i][j]

        return result