class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(k):
            l=0
            freq={}
            count=0
            for r in range(len(nums)):
                freq[nums[r]]=freq.get(nums[r],0)+1
                while len(freq)>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]

                    l=l+1
                count+=(r-l+1)
            return count
        return atmost(k)-atmost(k-1)

        