# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# O(n) Linear time approach using hashing

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = Counter(s)
        for i in res:
            if res[i] == 1:
                return s.index(i)
        return -1
