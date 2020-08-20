class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # BRUTE:
        # ans = []
        # low, high = int('1' + '0'*(N-1)), int('9'*N)
        # for num in range(low, high + 1):
        #     found = True
        #     for digit1, digit2 in zip(str(num), str(num)[1:]):
        #         if abs(int(digit1) - int(digit2)) != K:
        #             found = False
        #             break
        #     if found:
        #         ans.append(num)
        # return ans
        
        nums = [i for i in range(10)]
        for i in range(N-1):
            ans = []
            for x in nums:
                y = x%10
                if x>0 and y+K<10:
                    ans.append(x*10+y+K)
                if x>0 and K>0 and y-K>=0:
                    ans.append(x*10+y-K)
            nums = ans
        return nums