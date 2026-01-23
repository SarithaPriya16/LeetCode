class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getnext(num):
            total=0
            while num>0:
                digit=num%10
                total=total+digit*digit
                num//=10
            return total
        slow=n
        fast=getnext(n)
        while fast!=1 and slow!=fast:
            slow=getnext(slow)
            fast=getnext(getnext(fast))
        return fast==1
            
        
        