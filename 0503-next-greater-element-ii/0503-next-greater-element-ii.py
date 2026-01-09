class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        stack=[]
        res=[-1]*n
        for i in range(2*n-1,-1,-1):
            cur=nums[i%n]
            while stack and stack[-1]<=cur:
                stack.pop()
            if i<n:
                if stack:
                    res[i]=stack[-1]
            stack.append(cur)
        return res        