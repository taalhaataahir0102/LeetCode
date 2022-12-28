class Solution(object):
    def reverseWords(self, s):
        l = s.split(' ')
        ans = ''
        for i in l:
            ans+=i[::-1]+' '
        return ans[0:-1]
