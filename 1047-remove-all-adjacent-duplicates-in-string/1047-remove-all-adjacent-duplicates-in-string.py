class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for ch in s:
            if res and res[-1] == ch:
                res =res[:-1]
            else:
                res+=ch
        return res

        