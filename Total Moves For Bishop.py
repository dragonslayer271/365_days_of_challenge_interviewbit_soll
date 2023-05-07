class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self,row, column):


        topLeft = min(row, column) - 1

        bottomRight = 8 - max(row, column)

        topRight = min(row, 9-column) -1

        bottomLeft = 8 - max(row, 9-column)

        return (topLeft + topRight + bottomRight + bottomLeft)
