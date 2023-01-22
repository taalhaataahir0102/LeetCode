class Solution(object):
  def getCommon(self, nums1, nums2):
    p1 = 0
    p2 = 0
    l1 = len(nums1)
    l2 = len(nums2)
    for i in range(l1+l2):
      if nums1[p1] == nums2[p2]:
        return nums1[p1]
      elif nums1[p1] < nums2[p2] and p1 != l1-1:
        p1+=1
      elif nums1[p1] > nums2[p2] and p2 != l2-1:
        p2+=1
    return -1
