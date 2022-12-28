class Solution(object):
    def reverseStr(self, s, k):
        if k > len(s):
            return s[::-1]
        ans = ''
        for i in range(int(len(s)/k)):
            if i%2 == 0:
                new_s = s[i*k:(i*k)+k]
                ans += new_s[::-1]
            elif i%2 == 1:
                ans += s[i*k:(i*k)+k]
        if len(s)%k !=0:
            if (i+1)%2 == 0:
                new_s = s[-(len(s)%k):]
                ans+= new_s[::-1]
            else:
                ans+= s[-(len(s)%k):]
        return ans
