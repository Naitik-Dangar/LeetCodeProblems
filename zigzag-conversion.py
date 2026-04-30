import util

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        

        rows = [''] * numRows
        current_row = 0
        step = 1  
        
        for char in s:
            rows[current_row] += char
            
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
            
            current_row += step
            
        return "".join(rows)


def testCase(s, numRows):
    print("Input:\ns = ")
    print(s)
    print("numRows =")
    print(numRows)
    
    testSol = Solution()
    output = testSol.convert(s, numRows)
    print("Output: ")
    print(output)

util.printCaseHeader(1)
testCase("PAYPALISHIRING", 3)
util.printCaseHeader(2)
testCase("PAYPALISHIRING", 4)
util.printCaseHeader(3)
testCase("A", 1)
