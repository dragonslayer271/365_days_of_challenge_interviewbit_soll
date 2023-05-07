class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A=A.split()
        A=A[::-1]
        s=''
        for i in A:
            s+=i
            s+=' '
        return(s.strip())
