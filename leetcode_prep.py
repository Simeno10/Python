class Solution(object):
    def isValid(self, s):
        a = []
        n = len(s)
        for i in s:
            if (i=='(' or i == '{' or i == '['):
                a.append(i)
            else:
                if not a:
                    return False
                b = a.pop()
                if (i == ')' and b != '('):
                    return False
                if (i == ']' and b != '['):
                    return False
                if (i == '}' and b != '{'):
                    return False
        return len(a)==0
        """
        :type s: str
        :rtype: bool
        """
        
