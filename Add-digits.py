class Solution(object):
  def addDigits(self, num):
    while num - 10 >=0:
      l = list(str(num))
      for i in range(len(l)):
        l[i] = int(l[i])
      num = sum(l)
    return num
