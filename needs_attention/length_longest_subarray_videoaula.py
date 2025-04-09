class Solution:
    def maxsubarraylength(self, nums, k):
        res = 0
        count = {}

        esq = 0
        for dir, i in enumerate(nums):
            if nums[dir] in count:
                count[nums[dir]] += 1
            else:
                count[nums[dir]] = 1
            while count[nums[dir]] > k:
                count[nums[esq]] -= 1
                esq += 1
            res = max(res, dir - esq + 1)

        return res

    # [10,12,12,12] k = 3 -> 4
    # [1,1,1,3] k = 2
nums = [1,1,1,3]
k = 2
Solution().maxsubarraylength(nums, k)