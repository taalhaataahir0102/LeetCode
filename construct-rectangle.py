class Solution(object):
    def constructRectangle(self, area):
        L = int(math.ceil(math.sqrt(area)))
        W = int(math.floor(math.sqrt(area)))
        while L*W !=area:
            if L*W < area:
                L+=1
            elif L*W > area:
                W-=1
        return [L,W]
 
