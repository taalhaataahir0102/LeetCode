class Solution(object):
  def moveZeroes(self, nums):
    prev = 0
    for i in range(1,len(nums)):
      if nums[prev] == 0 and nums[i] != 0:
        nums[prev], nums[i] = nums[i], nums[prev]
      if nums[prev] !=0:
        prev +=1
    return nums
