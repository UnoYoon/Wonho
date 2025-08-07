# 1. nums 배열이 존재 -> 정수형 target이 배열안에 존재하는지 체크
# 2. if  존재한다면 그대로 nums 값을 출력, else -1 출력
# 3. O(logn) 시간복잡도를 이용해 해결 -> 특정 위치의 값을 찾는 것이니 이분 탐색!

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (end - start) // 2 


        for _ in range(mid + 1):
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                start += 1
                end -= 1
        
        return -1