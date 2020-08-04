import math as m
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # if num==0:
        #     return False
        # while num!=1:
        #     if num%4!=0:return False
        #     num = num//4
        # return True
        
        # Follow up: Do it without loops.
        
        # Observations: 
        #     1. binary representation of power 4's includes single 1.
        #     2. followed by even number of 0's
        
        temp = bin(num)[3:]
        return (num!=0) and ('1' not in temp) and len(temp)%2==0