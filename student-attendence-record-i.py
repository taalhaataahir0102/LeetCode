class Solution(object):
    def checkRecord(self, s):
        counter= 0
        l = len(s)
        for i in range(len(s)):
            if s[i] == 'A':
                counter+=1
            if counter == 2:
                return False
            if s[i] == 'L' and (i+2) < l and (s[i+1] == 'L' and s[i+2] == 'L'):
                return False
        return True
