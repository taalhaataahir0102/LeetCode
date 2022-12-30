class Solution(object):
    def distributeCandies(self, candyType):
        total_type = len(set(candyType))
        max_candy = int(len(candyType)/2)
        if total_type <= max_candy:
            return total_type
        else:
            return max_candy
