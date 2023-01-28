class Solution(object):
  def judgeCircle(self, moves):
    ans = [0,0]
    for i in moves:
      if i == "L":
        ans[0]-=1
      if i == "R":
        ans[0]+=1
      if i == "D":
        ans[1]-=1
      if i == "U":
        ans[1]+=1
    if ans == [0,0]:
      return True
    return False
