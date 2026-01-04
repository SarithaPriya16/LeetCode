class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(k):
            l=0
            count=0
            odd=0
            for r in range(len(nums)):
                if nums[r]%2 == 1:
                    odd+=1
                while odd>k:
                    if nums[l]%2==1:
                        odd-=1
                    l=l+1
                count=count+(r-l+1)
            return count
        return atmost(k)-atmost(k-1)
            
        