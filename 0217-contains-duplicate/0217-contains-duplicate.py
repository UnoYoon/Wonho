# 배열 속에 어떠한 값이 최소 2번 이상 갖고있기.

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)

        for value in nums_count.values():
            if value > 1:
                return True
        return False