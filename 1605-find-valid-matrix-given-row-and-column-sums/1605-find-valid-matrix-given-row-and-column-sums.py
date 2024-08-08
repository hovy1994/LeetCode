class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        rowLen = len(rowSum)
        colLen = len(colSum)
        
        result = [[0 for _ in range(colLen)] for _ in range(rowLen)]
        
        for i in range(rowLen):
            for j in range(colLen):
                min_value = min(rowSum[i], colSum[j])
                result[i][j] = min_value
                rowSum[i] -= min_value
                colSum[j] -= min_value
        
        return result
