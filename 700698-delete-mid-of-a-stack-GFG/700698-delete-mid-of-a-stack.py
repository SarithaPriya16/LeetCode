class Solution:
    def deleteMid(self, stack):
        #code here
        temp=[]
        n=len(stack)
        mid=n//2
        for _ in range(mid):
            temp.append(stack.pop())
        stack.pop()
        while temp:
            stack.append(temp.pop())
        return stack
        
            