class Solution(object):
    def isPalindrome(self, s):
        word = s = ''.join(e for e in s if e.isalnum()).lower()
        word = word[::-1]
        return word == s
