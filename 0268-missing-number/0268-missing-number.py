class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = n * (n + 1) // 2

        s2 = 0
        for i in nums:
            s2 += i

        return total_sum - s2
