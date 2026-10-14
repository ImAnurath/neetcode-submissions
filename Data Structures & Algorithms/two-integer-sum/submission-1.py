class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            remain = target - num
            if remain in seen:
                return [seen[remain], idx]
            seen[num] = idx