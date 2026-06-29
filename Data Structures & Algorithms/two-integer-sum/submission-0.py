

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for i, num in enumerate(nums):

            if (target - num) in h:

                return [h.get(target - num), i]

            else:

                h[num] = i
        
        
        