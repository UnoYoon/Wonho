# nums 안에 있는 0을 만나면 뒤로 보낸다. -> 0을 제거하고 그 수만큼 리스트에 추가해도 된다.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for num in nums:
            if nums != 0:
                nums[insert_pos] = num
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = 0