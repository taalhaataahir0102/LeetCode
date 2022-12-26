class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_len = 0
        curr_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_len +=1
            elif nums[i] == 0:
                curr_len = 0
            if max_len<curr_len:
                max_len = curr_len
        return max_len
