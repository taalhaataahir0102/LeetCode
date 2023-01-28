class Solution(object):
  def findLengthOfLCIS(self, nums):
    print(nums)
    p1 = 0
    p2 = 1
    longest = 1
    current = 1
    for i in range(len(nums)-1):
      if nums[p1]<nums[p2]:
        current+=1
        p1+=1
        p2+=1
      else:
        p1 = p2
        p2+=1
        if current>longest:
          longest = current
        current = 1
    if current> longest:
      longest = current
    return longest
