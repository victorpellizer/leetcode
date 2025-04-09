class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            esq = i + 1
            dir = len(nums) - 1
            while esq < dir:
                soma_tripla = a + nums[esq] + nums[dir]
                if soma_tripla > 0:
                    dir -= 1
                elif soma_tripla < 0:
                    esq += 1
                else:
                    res.append([a, nums[esq], nums[dir]])
                    esq += 1
                    while nums[esq] == nums[esq-1] and esq < dir:
                        esq += 1
        return res