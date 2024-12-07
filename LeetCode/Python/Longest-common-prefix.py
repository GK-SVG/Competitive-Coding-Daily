# https://leetcode.com/problems/longest-common-prefix/description/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        first = strs[0]
        prefix = ""
        for word in strs[1:]:
            for i in range(len(word)):
                if first[:i+1] == word[:i+1]:
                    prefix = first[:i+1]
                else:
                    prefix = ""
        return prefix
    

obj = Solution()
print(obj.longestCommonPrefix(["a","a","b"]))