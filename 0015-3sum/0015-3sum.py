# 3개의 값을 합해서 0이 나오는 값 3개를 출력해라(여러 개도 가능)
# 그런데 인덱스는 다르더라도 값이 합쳐지는 과정에서 0, 1, -1 / 1, -1, 0 이런 식이면 그냥 0, 1, -1 하나만 출력 
# 3개의 포인터가 있어야하나?

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result