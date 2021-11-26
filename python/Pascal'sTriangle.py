def generate(self, numRows: int) -> List[List[int]]:
    
    ans = [[1]]
    for i in range( 1, numRows):
        lst = [1] * (i + 1)
        for j in range( 1, i):
            lst[j] = ans[i - 1][j] + ans[i - 1][j - 1]
        ans.append(lst)
    return ans