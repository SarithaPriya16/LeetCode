class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []

        freq1 = {}
        freq2 = {}
        res = []

        # frequency of p
        for ch in p:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1

        k = len(p)

        # first window frequency
        for i in range(k):
            freq2[s[i]] = freq2.get(s[i], 0) + 1

        # check first window
        if freq1 == freq2:
            res.append(0)

        l = 0

        # slide the window
        for r in range(k, len(s)):
            freq2[s[r]] = freq2.get(s[r], 0) + 1

            freq2[s[l]] -= 1
            if freq2[s[l]] == 0:
                del freq2[s[l]]
            l += 1

            if freq1 == freq2:
                res.append(l)

        return res
