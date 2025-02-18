class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum=0
        for char in operations:
            if '+' in char:
                sum+=1
            else:
                sum-=1
        return sum