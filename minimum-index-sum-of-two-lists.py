class Solution(object):
    def findRestaurant(self, list1, list2):
        common = list(set(list1).intersection(list2))
        d1 = {} 
        d2 = {}
        for i in range(len(list1)):
            d1[list1[i]] = i
        for i in range(len(list2)):
            d2[list2[i]] = i
        ans = []
        check = 2001
        for i in common:
            if d1[i] + d2[i] < check:
                check = d1[i] + d2[i]
                ans = []
                ans.append(i)
            elif d1[i] + d2[i] == check:
                check = d1[i] + d2[i]
                ans.append(i)
        return ans
