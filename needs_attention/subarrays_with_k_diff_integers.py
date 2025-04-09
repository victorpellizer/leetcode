class Solution:
    def subarraysWithKDistinct(self, nums: int, k: int) -> int:
        subarrays = []

        index = 0
        while index < len(nums):
            diff_nbrs = []
            while len(diff_nbrs) <= k:
                diff_nbrs.append(nums[index])
                index += 1
            subarrays.append(diff_nbrs)
            if index == len(nums):
                break
            index -= 1
        
        subarray = []
        while len(diff_nbrs) <= k:
            subarray.append(nums[index])


        print(subarrays)
        
# nums = [1,2,1,2,3], k = 2
# [1,2], [1,2,1], [1,2,1,2], [2,1], [2,1,2], [1,2], [2,3]
# dado um array com inteiros e um número K
# retornar quantidade de bons subarrays
# subarray é bom quando tem exatamente K números diferentes
#

nums = [1,2,1,2,3]
k = 2
Solution().subarraysWithKDistinct(nums, k)