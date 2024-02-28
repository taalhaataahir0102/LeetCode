class Solution(object):
  def findTheDifference(self, s, t):
    d = {key: 0 for key in t}
    for i in t:
      d[i] += 1
    for i in s:
      d[i] -= 1
    for key in d:
      if d[key] == 1:
        return key
    return
