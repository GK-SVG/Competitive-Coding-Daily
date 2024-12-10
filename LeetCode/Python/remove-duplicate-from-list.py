# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_count = 0
        temp_list = []

        for item in nums:
            if item not in temp_list:
                temp_list.append(item)
            else:
                duplicate_count += 1
        
        unique_count = len(temp_list)

        for i in range(duplicate_count):
            temp_list.append("_")
        
        return unique_count, temp_list

   