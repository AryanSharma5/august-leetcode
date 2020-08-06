class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # O(N) TIME and O(1) SPACE
        
        ans = []
        if not nums:
            return ans
        maxi = max(nums)
        for i in range(len(nums)):
            nums[i] -= 1
        for i in range(len(nums)):
            newIdx = nums[i]%maxi
            nums[newIdx] += maxi
        for i in range(len(nums)):
            if nums[i]//maxi == 2:
                ans.append(i+1)
        return ans