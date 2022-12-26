class Solution(object):
    def licenseKeyFormatting(self, s, k):
        st = s.replace('-','').upper()
        new_st = st[0:len(st)%k]
        if len(new_st)>0:
            new_st += '-'
        for i in range(len(st)%k,len(st),k):
            new_st+=st[i:i+k]
            new_st+= '-'
        return new_st[0:-1]
