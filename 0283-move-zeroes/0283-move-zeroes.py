# nums 안에 있는 0을 만나면 뒤로 보낸다. -> 0을 제거하고 그 수만큼 리스트에 추가해도 된다.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        nums[:] = [x for x in nums if x != 0]
        nums.extend([0] * count)