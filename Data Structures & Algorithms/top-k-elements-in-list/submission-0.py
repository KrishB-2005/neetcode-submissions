from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        s = []
        new = Counter(nums)

        new = new.most_common()
        
        for i in range(k):
            s.append(new[i][0])

        return s


            
            
