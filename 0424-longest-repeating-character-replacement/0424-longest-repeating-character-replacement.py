class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq={}
        l=0
        max_len=0
        max_freq=0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            max_freq=max(max_freq,freq[s[r]])
            if (r-l+1)-max_freq > k:
                freq[s[l]]-=1
                l=l+1
            max_len=max(max_len,r-l+1)
        return max_len
        
        