#  자신을 제외한 수를 다 곱해서 값을 치환해주기.
# EX1) 1 : 2 * 3 * 4 = 24 | 2 : 1 * 3 * 4 = 12
# EX2) -1 : -1 * 0 * -3 * -3 = 0

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        p = 1
        for i in range(len(nums)):
            answer.append(p)
            p *= nums[i]
        
        p = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= p
            p *= nums[i]

        return answer