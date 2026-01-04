class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        count=0
        freq={'a':0,'b':0,'c':0}
        n=len(s)

        for r in range(n):
            freq[s[r]]+=1
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                count+=(n-r)
                freq[s[l]]-=1
                l=l+1
            
        return count
    

        