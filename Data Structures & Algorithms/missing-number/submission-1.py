class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        j = 0

        list.sort(nums)

        for i in range(len(nums)):

            if nums[i] != j:
                return j
            else:
                j += 1
                continue
        
        return j