class Solution(object):
    def applyGravity(self, box, col):
        l = r = len(box)-1
        
        while(r>0 and l>=0):
            if box[r][col]!=".":
                r-=1
                continue
            
            if l>=r:
                l = r-1
            if box[l][col]=="#":
                box[r][col]="#"
                box[l][col]="."
                r-=1  
            elif box[l][col]=="*":
                r=l-1
                l=r-1
            else:
                l-=1
        
            
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        rowLen = len(box)
        rotatedBox = [['.' for _ in range(rowLen)] for _ in range(len(box[0]))]
        for i in range(rowLen):
            for j in range(len(box[0])):
                rotatedBox[j][rowLen-i-1]=box[i][j]
        
        
        for i in range(len(rotatedBox[0])):
            self.applyGravity(rotatedBox, i)
            
        return rotatedBox