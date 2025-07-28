# 질문: 만약에 갖고 있는 수가 4, 4, 4, 4, 5, 5, 5, 5, 1이면 4, 5를 출력하나요? 순서는 어떻게 해야하나요?
# 배열의 값이 2억이야. 그럼 O(n)은 이미 늦다.
# O(logn)으로 처리가능한 값을 만들어야할 듯
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = Counter(nums)

        max_nums = count_nums.most_common(1)[0][0]
        return max_nums