class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        counter = {}
        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        for j in t:
            if j not in counter:
                return False
            counter[j] -= 1
            if counter[j] < 0:
                return False
        return True
