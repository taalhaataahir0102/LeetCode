class Solution(object):
    def findRelativeRanks(self, score):
        ans = []
        a = score[:]
        score.sort(reverse=True)
        for i in range(len(a)):
            ind = score.index(a[i])
            if ind == 0:
                ans.append('Gold Medal')
            elif ind == 1:
                ans.append('Silver Medal')
            elif ind == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(ind+1))
        return ans
