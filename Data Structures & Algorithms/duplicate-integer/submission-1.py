class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        non_dup = set(nums)

        return len(nums) != len(non_dup)

        