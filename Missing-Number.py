class Solution(object):
  def missingNumber(self, nums):
    new = [-1]*len(nums)
    new.append(-1)
    for i in range(len(nums)):
      new[nums[i]] = 1
    return new.index(-1)
