class Solution(object):
    def findDuplicates(self, nums):
       freq={}
       ans=[]
       for num in nums:
           if num in freq:
              ans.append(num)
           else:
              freq[num]=1
       return ans
        