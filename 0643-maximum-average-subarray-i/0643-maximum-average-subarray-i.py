class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Initial window sum
        w_sum = sum(nums[:k])
        max_sum = w_sum

        # Slide the window
        for i in range(k, len(nums)):
            w_sum = w_sum + nums[i] - nums[i - k]
            if w_sum > max_sum:
                max_sum = w_sum

        # Return maximum average
        return max_sum / float(k)
