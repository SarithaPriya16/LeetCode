class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vow={'a','e','i','o','u'}
        l=0
        count=0
        for i in range(k):
            if s[i] in vow:
                count+=1
        max_count=count
        for r in range(k,len(s)):
            if s[r] in vow:
                count+=1
            if s[l] in vow:
                count-=1
            l=l+1
            max_count=max(max_count,count)
        return max_count

            
            
