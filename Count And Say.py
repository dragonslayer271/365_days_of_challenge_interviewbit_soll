class Solution:
    # @param A : integer
    # @return a string
    def countAndSay(self, A):
        if A == 1:
            return "1"
        
        array_one = "1"
        for _ in range(2, A+1):
            j = 0
            array_two = ""
            while j < len(array_one):
                count = 1
                while j+1 < len(array_one) and array_one[j] == array_one[j+1]:
                    j += 1
                    count += 1
                array_two += str(count) + str(array_one[j])
                j += 1
            array_one = array_two
        
        return array_one
