class Solution(object):
  def isPowerOfTwo(self, n):
    n1 = 0
    i = 0
    while n1 < n:
      n1 = pow(2,i)
      i+=1
      if n1 == n:
        return True
    return False
 
