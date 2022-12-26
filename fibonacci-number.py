class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        s = [1,1]
        for i in range(n-2):
            s.append(s[i]+s[i+1])
        return s[-1]
