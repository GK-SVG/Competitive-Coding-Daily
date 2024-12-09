from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        temp = 0
        for item1, item2 in zip_longest(a[::-1],b[::-1], fillvalue='0'):
        
            if temp == 1:
                addition = int(item1) + int(item2) + temp
                if addition == 0:
                    temp = 0
                    output += '0'
                elif addition == 1:
                    temp = 0
                    output += '1'
                elif addition == 2:
                    temp = 1
                    output += '0'
                elif addition == 3:
                    temp = 1
                    output += '1'
            else:
                addition = int(item1) + int(item2)
                if addition == 0:
                    temp = 0
                    output += '0'
                elif addition == 1:
                    temp = 0
                    output += '1'
                elif addition == 2:
                    temp = 1
                    output += '0'
        if temp:
            output += "1"
            
        return output[::-1]

obj = Solution()
print(obj.addBinary("100", "1100"))