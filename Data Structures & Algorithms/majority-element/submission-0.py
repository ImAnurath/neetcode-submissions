class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        for num in nums:
            ht[num] = ht.get(num, 0) + 1
        return max(ht, key = ht.get)
        