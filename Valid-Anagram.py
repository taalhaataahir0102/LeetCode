class Solution(object):
  def isAnagram(self, s, t):
    d = {}
    for i in s:
      d[i]=0
    for i in s:
      d[i]+=1
    for i in t:
      if i not in d:
        return False
      d[i] -=1
    if list(d.values()) == [0]*len(set(s)):
      return True
    return False
 
