class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={0:1}
        currentsum=0
        count=0
        for num in nums:
            currentsum+=num
            if currentsum-k in freq:
                count+=freq[currentsum-k]
            freq[currentsum]=freq.get(num,0)+1
        return count
