class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for digit in num:
            while stack and k>0 and stack[-1]>digit:
                stack.pop()
                k=k-1
            stack.append(digit)
        while k>0:
            stack.pop()
            k-=1
        leading_zero=True
        res=""
        for ch in stack:
            if leading_zero and ch=='0':
                continue
            leading_zero=False
            res+=ch
        return res if res else "0"
        