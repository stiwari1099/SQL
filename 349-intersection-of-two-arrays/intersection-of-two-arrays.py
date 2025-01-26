class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        num1_set=set(nums1) #1,2
        num2_set=set(nums2) #2

        for num in num1_set:
            if num in num2_set:
                res.append(num)
        return res

        