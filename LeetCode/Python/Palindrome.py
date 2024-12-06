# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        
        temp = x
        num = ""
        while x>0:
            remainder = x%10
            num += f"{remainder}"
            x = x//10
        if int(num) == temp:
            return True
        else:
            return False
        
obj = Solution()
print(obj.isPalindrome(0))

# Best Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]