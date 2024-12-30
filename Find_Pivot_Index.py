class Solution(object):
    def pivotIndex(self, nums):
        total_sum = 0
        for num in nums:
            total_sum += num
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        return -1


        