class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        all_num = set(range(1,n+1))
        num_set = set(nums)

        missing_num = list(all_num-num_set)

        return missing_num
