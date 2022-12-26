class Solution(object):
    def findWords(self, words):
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        ans = []
        for i in words:
            check = []
            for j in i:
                if j in first:
                    check.append(1)
                elif j in second:
                    check.append(2)
                elif j in third:
                    check.append(3)
            if len(set(check)) == 1:
                ans.append(i)
        return ans
