class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCountMap = {}
        for c in s:
            sCountMap[c] = sCountMap.get(c, 0) + 1
        tCountMap = {}
        for c in t:
            tCountMap[c] = tCountMap.get(c, 0) + 1
        for k, v in sCountMap.items():
            if v != tCountMap.get(k, 0):
                return False
        return True
