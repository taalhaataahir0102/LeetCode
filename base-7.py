class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return '0'
        s= ''
        check = True
        if num <0:
            num = abs(num)
            check = False
        while num!=0:
            s += str(num%7)
            num = int(num/7)
        if check == False:
            s += '-'
        return s[::-1]
