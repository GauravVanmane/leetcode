#Solution1
        initial_dic = {}
        
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in initial_dic.keys():
                    initial_dic[s[i]] = 1
                else:
                    initial_dic[s[i]] += 1
            print(initial_dic)
            for j in range(len(t)):
                if t[j] not in initial_dic.keys():
                    return False
                else:
                    if initial_dic[t[j]] < 1:
                        return False
                    initial_dic[t[j]] -= 1
            return True
        return False

        #Solution 2:

        return Counter(s) == Counter(t)

        #Solution 3:
        return sorted(t) == sorted(s)
