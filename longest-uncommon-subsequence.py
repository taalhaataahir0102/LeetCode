class Solution(object):
    def findLUSlength(self, a, b):
        if len(a) > len(b):
            return len(a)
        elif len(a) < len(b):
            return len(b)
        while a in b:
            if len(a) == 0:
                return -1
            a = a[0:-1]
        return len(a)
