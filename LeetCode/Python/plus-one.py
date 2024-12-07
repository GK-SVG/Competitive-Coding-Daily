# https://leetcode.com/problems/plus-one/

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp_str = ""
        for item in digits:
            temp_str += f"{item}"

        plus_one = int(temp_str) + 1
        return [int(char) for char in str(plus_one)]

obj = Solution()

print(obj.plusOne([9,9]))