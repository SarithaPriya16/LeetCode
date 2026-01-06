class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        freq1={}
        l=0
        for ch in stones:
            if ch in freq1:
                freq1[ch]+=1
            else:
                freq1[ch]=1
        freq2={}
        for ch in jewels:
            if ch in freq2:
                freq2[ch]+=1
            else:
                freq2[ch]=1
        count=0
        for ch in freq2:
            if ch in freq1:
                count=count+freq1[ch]
        return count
        
