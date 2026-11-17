class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        a=set()
        for num in nums:
            if num in a:
                return num
            a.add(num)