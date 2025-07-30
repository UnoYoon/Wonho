# 가장 큰 합을 만들 수 있는 가장 긴 부분 배열을 찾아라.
# 1. 가장 길 것 
# 2. 큰 수 일 것
# Example 3를 보면 24가 가장 큰 수이지만 -> [5, 4, 7, 8] ////  23 -> [5, 4, -1, 7, 8]  

# 애초에 Subarray : 연속된 인덱스 구간

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        
        return max(nums)


    # nums[i]                5 4 -1 7 8
    # nums[i] + nums[i - 1]  5 9 -1 7  8   i = 1
    #                        5 9  8 7  8   i = 2
    #                        5 9  8 15 8   i = 3
    #                        5 9  8 15 23  i = 4
