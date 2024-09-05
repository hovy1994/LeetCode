class Solution(object):
   def missingRolls(self, rolls, mean, n):
        n_sum = mean*(len(rolls)+n) - sum(rolls)
        base = int(n_sum/n)
        result = [base]*n
        remainder = n_sum%n
        
        if n_sum < n or n_sum > 6 * n:
            return []
        
        for i in range(remainder):
            result[i]+=1
        
        return result