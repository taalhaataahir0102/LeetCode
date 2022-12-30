class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        ans = 0
        curr = 0
        dic = {}
        for i in nums:
            dic[i] = 0
        for i in nums:
            dic[i] +=  1
        for i in range(len(nums)):
            if nums[i]+1 in dic:
                curr = dic[nums[i]] + dic[nums[i]+1]
            if ans < curr:
                ans = curr
        return ans 
