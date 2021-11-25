def romanToInt(self, s: str) -> int:
    map_num = {"I":1, "V":5, "X":10, "L": 50, "C":100, "D": 500,"M":1000}
    n = len(s)
    output = map_num[s[n-1]]
    for i in range(n-2, -1, -1):
        if map_num[s[i]] >= map_num[s[i+1]]:
            output += map_num[s[i]]
        else:
            output -= map_num[s[i]]
    return output