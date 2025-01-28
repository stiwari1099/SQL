class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        all_num = set(range(1,len(nums)+1))
        num_set = set(nums)

        missing_num = list(all_num-num_set)

        return missing_num
