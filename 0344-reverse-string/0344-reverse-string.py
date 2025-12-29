class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        # Loop until the pointers meet
        while left < right:
            # 🔹 Swap s[left] and s[right] here
            s[left],s[right]=s[right],s[left]

            # Move pointers
            left += 1
            right -= 1
            

