class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
            temp = [1]
            for j in range(1, i+1):
                if i==j:
                    temp.append(1)
                else:
                    temp.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(temp)
        return ans[rowIndex]