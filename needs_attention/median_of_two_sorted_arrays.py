class Solution:
    def findMedianSortedArrays(self, array1, array2) -> float:
        merged_list = array1 + array2
        merged_list.sort()
        len_list = len(merged_list)
        median_index = int((len_list-1) / 2)
        if (len_list % 2):
            answer = merged_list[median_index]
        else:
            answer = (merged_list[median_index] + merged_list[median_index + 1])/2.0
        print(answer)
        return answer


# nums1 = [1,3]
# nums2 = [2]
nums1 = [1,2]
nums2 = [3,4]
Solution().findMedianSortedArrays(nums1, nums2)