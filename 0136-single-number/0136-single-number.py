# 배열에서 하나인 수만 찾으면 된다. 
# 하나의 수는 하나만 있는 것

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = Counter(nums)

        for num, count in nums_count.items():
            if count == 1:
                return num
