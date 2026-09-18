class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, k = 0, 1, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums.insert(left + 1, nums[right])
                left += 1
                right += 1
                k += 1
        return k