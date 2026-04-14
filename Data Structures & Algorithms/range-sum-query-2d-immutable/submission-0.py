class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.matrix = matrix

        self.PrefixSumMatrix = [[0]*(len(self.matrix[0])+1) for _ in range (len(matrix)+1)]

        for r in range(len(self.matrix)):
            prefix = 0
            for c in range((len(self.matrix[0]))):
                prefix +=self.matrix[r][c]
                above = self.PrefixSumMatrix[r][c+1] 
                self.PrefixSumMatrix[r+1][c+1] = prefix+above


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        r1,c1,r2,c2=row1+1,col1+1,row2+1,col2+1

        bottomRight = self.PrefixSumMatrix[r2][c2]
        above = self.PrefixSumMatrix[r1-1][c2]
        left = self.PrefixSumMatrix[r2][c1-1]
        topLeft = self.PrefixSumMatrix[r1-1][c1-1]

        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)