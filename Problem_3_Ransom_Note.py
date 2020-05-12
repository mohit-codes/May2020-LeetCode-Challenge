"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
"""

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(ransomNote == magazine or len(ransomNote) == 0): return True
        else:
            mg = Counter(magazine)
            rn = Counter(ransomNote)
            # print(mg)
            # print(rn)
            flag = True
            for i in rn:
                if mg[i] < rn[i] :
                    flag = False
                    # print(i," magazine = ",mg[i],"ransom = ",rn[i])
                    break
            return flag
