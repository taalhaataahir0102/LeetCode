class Solution(object):
    def detectCapitalUse(self, word):
        countu = 0
        countl = 0
        for i in word:
            if i == i.upper():
                countu+=1
            elif i == i.lower():
                countl+=1
        if countu == len(word) or countl == len(word):
            return True
        elif countu == 1 and countl == len(word)-1 and word[0] == word[0].upper():
            return True
        return False
