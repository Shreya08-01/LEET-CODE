class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index : int)->None:
            if index == length:
                result.append(current_permutation[:])
                return
            for j in range(length):
                if visited[j]:
                    continue
                if j>0 and nums[j]==nums[j-1] and not visited[j-1]:
                    continue
                current_permutation[index]=nums[j]
                visited[j]=True
                backtrack(index+1)
                visited[j]=False
        length=len(nums)
        nums.sort()
        result=[]
        current_permutation=[0]*length
        visited=[False]*length
        backtrack(0)
        return result