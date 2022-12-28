class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        s = 0
        for i in range(int(len(nums)/2)):
            s += min(nums[i*2],nums[(i*2)+1])
        return s
