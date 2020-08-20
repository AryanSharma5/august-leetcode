class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        arr = [0]*num_people
        i=0
        while candies>0:
            arr[i%num_people] += (i+1) if i+1<candies else candies
            candies -= (i+1)
            i += 1
        return arr