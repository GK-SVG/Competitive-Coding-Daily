# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = len(nums)
        output = []
        for i in range(end):
            start = i+1
            for j in range(start, end):
                addition = nums[i] + nums[j]
                if addition == target:
                    if i != j:
                        output.append(i)
                        output.append(j)
        return output


obj = Solution()

print(obj.twoSum([2,7,11,15], 9))