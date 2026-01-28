class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lower_bound(nums,target):
            low=0
            high=len(nums)-1
            ans=len(nums)
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def upper_bound(nums,target):
            low=0
            high=len(nums)-1
            ans=len(nums)
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        first=lower_bound(nums,target)
        if first==len(nums) or nums[first]!=target:
            return [-1,-1]
        last=upper_bound(nums,target)-1
        return [first,last]
                
                
        