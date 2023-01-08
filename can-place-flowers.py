class Solution(object):
  def canPlaceFlowers(self, flowerbed, n):
    if n == 0:
        return True
    if len(flowerbed) == 1 and flowerbed[0] == 0 and n ==1:
        return True
    if flowerbed[0:2] == [0,0] and n>=1:
        flowerbed[0] = 1
        n-=1
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n-=1
        if n == 0:
            return True
    if flowerbed[-2:] == [0,0]:
        flowerbed[-1] = 1
        n -=1
    if n == 0:
        return True
    else:
        return False
