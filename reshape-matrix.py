class Solution(object):
    def matrixReshape(self, mat, r, c):
        if r*c != len(mat)*len(mat[0]):
            return mat
        flatten = []
        ans = []
        for i in mat:
            for j in i:
                flatten.append(j)
        for i in range(r):
            ans.append(flatten[i*c:(i*c)+c])
        return ans
