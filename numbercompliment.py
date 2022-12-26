class Solution(object):
    def findComplement(self, num):
        b = bin(num)[2:]
        for i in range(len(b)):
          if b[i] == '0':
            list1 = list(b)
            list1[i] = '1'
            b = ''.join(list1)
          elif b[i] == '1':
            list1 = list(b)
            list1[i] = '0'
            b = ''.join(list1)
        return int(b,2)
 
