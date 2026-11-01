class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for y in range(i+1,len(nums)):
                if nums[i]+nums[y] == target:
                    return [i,y]