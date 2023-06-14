class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):
        if A <= 1:
            return 0
 
        max_div = math.floor(math.sqrt(A))
        for i in range(2, 1 + max_div):
            if A % i == 0:
                return 0
        return 1
        
