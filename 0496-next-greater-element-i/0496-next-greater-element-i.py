class Solution(object):
    def nextGreaterElement(self,nums1, nums2):
        stack = []
        nge_map = {}

    # Step 1: Process nums2
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                nge_map[nums2[i]] = stack[-1]
            else:
                nge_map[nums2[i]] = -1

            stack.append(nums2[i])

    # Step 2: Build answer for nums1
        result = []
        for num in nums1:
            result.append(nge_map[num])

        return result
