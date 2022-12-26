class Solution(object):
    def checkPerfectNumber(self, num):
        if num == 1:
            return False
        s= 1
        for i in range(2,int(math.sqrt(num))+1):
            if num/float(i) == int(num/i):
                s+=i+int(num/i)
        if s == num:
            return True
        return False
