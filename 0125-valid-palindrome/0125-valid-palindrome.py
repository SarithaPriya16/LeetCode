class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert string to lowercase
        s = s.lower()
        
        # Keep only alphanumeric characters
        new_s = ""
        for ch in s:
            if ch.isalnum():
                new_s += ch

        # Two pointers
        left = 0
        right = len(new_s) - 1

        while left < right:
            if new_s[left] != new_s[right]:
                return False  # Not a palindrome
            left += 1
            right -= 1

        return True  # Palindrome
