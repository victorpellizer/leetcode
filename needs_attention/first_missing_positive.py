class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        nums.sort()
        for num in nums:
            if smallest == num:
                smallest += 1
        if smallest == len(nums) and smallest in nums:
            smallest += 1
        return smallest

array = [7,8,9,11,12]
# array = [3,4,-1,1]
# array = [1,2,0]
Solution().firstMissingPositive(array)