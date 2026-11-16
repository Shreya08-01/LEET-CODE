class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
       max_wealth=0
       for customer in accounts:
          total=sum(customer)
          if total>max_wealth:
            max_wealth=total
       return max_wealth