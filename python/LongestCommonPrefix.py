def longestCommonPrefix(self, strs: List[str]) -> str:
    output = ""
    if len(strs) == 0:
        return output
    minimum = len(strs[0])
    for i in range(1, len(strs)):
        minimum = min(minimum, len(strs[i]))
    for i in range(0, minimum):
        current = strs[0][i]
        for j in range(0, len(strs)):
            if strs[j][i] != current: 
                return output
        output += current
    return output