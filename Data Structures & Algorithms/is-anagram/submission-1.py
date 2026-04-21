class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(t) == Counter(s) 
        