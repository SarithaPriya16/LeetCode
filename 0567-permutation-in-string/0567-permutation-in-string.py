class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        freq1={}
        freq2={}
        for ch in s1:
            if ch in freq1:
                freq1[ch]+=1
            else:
                freq1[ch]=1
        k=len(s1)
        for i in range(k):
            freq2[s2[i]]=freq2.get(s2[i],0)+1
        if freq1 == freq2:
            return True
        l=0
        for r in range(k,len(s2)):
            freq2[s2[r]]=freq2.get(s2[r],0)+1
            freq2[s2[l]]-=1
            if freq2[s2[l]]==0:
                del freq2[s2[l]]
            l=l+1
            if freq1==freq2:
                return True
        return False

        