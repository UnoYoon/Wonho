# 0부터 n까지 1씩 증가하는 수가 존재. 하지만 없는 수 단 하나 : Missing number
# 무조건 0부터 시작

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums.sort()
        
        for i in range(max_num + 1):
            if i == nums[i]:
                continue
            else:
                return i
        return max_num + 1