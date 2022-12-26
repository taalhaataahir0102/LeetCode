class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                ans.append(-1)
            else:
                ind = nums2.index(nums1[i])
                check = True
                for j in range(ind,len(nums2)):
                    if nums2[j]>nums2[ind]:
                        ans.append(nums2[j])
                        check = False
                        break
                if check == True:
                    ans.append(-1)
        return ans
