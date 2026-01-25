class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq={}
        seen=[]
        for num in nums1:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in nums2:
            if freq.get(num,0)>0:
                seen.append(num)
                freq[num]-=1
        return seen
            
    
        