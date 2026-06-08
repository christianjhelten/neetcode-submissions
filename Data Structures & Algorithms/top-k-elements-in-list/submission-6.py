from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        output = []
        for num, freq in count.most_common(k):   # k most frequent, as (value, count) pairs
            output.append(num)
        return output