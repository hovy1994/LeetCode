class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a
    
    def lcd(self, a, b):
        gcd = self.gcd(a,b)
        return gcd*int(a/gcd)*int(b/gcd)
    
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        
        left = 1
        right = 10**10
        lcd = self.lcd(divisor1, divisor2)
        while left<right:
            mid = (left+right)>>1
            
            cnt1 = mid - int(mid/divisor1)
            cnt2 = mid - int(mid/divisor2)
            totalCnt = mid - int(mid/lcd)
            
            if cnt1>=uniqueCnt1 and cnt2>=uniqueCnt2 and totalCnt >=uniqueCnt1+uniqueCnt2:
                right = mid
            else:
                left = mid+1
                
        return right