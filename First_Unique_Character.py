class Solution(object):
  def firstUniqChar(self, s):
    d = {key: 0 for key in s}
    for i in s:
      d[i] +=1
    for i,c in enumerate(s):
      if d[c] == 1:
        return i
    return -1
