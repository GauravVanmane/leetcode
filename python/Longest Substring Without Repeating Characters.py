def lengthOfLongestSubstring(self, s: str) -> int:
    i, j, hashset = 0, 0, []
    max_n = 0
    
    while j < len(s):
        if s[j] not in hashset:
            hashset.append(s[j])
            j += 1
            max_n = max(len(hashset), max_n)
        else:
            hashset.remove(s[i])
            i += 1
    
    return max_n