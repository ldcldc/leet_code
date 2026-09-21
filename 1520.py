class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        len_char = dict()
        for i in range(len(s)):
            if s[i] not in len_char:
                len_char[s[i]] = [i,i]
            else:
                len_char[s[i]][1] = i

        temp = list(len_char.items())[:]
        visited = set()
        
        print(len_char)
        
        for c, l in temp:
            if c not in visited:
                visited.add(c)
                
                start = l[0] + 1
                end = l[1]
                del_list = set()
                
                while(start < l[1]):
                    if s[start] in len_char:
                        if l[1] < len_char[s[start]][1]:
                            if l[0] < len_char[s[start]][0]:
                                l[1] = len_char[s[start]][1]
                                visited.add(s[start])
                                del_list.add(s[start])
                            else:
                                del_list.add(c)
                    else:
                        del_list.add(c)
                    start += 1
                for del_c in del_list:
                    del len_char[del_c]
        
        len_char = list(sorted(len_char.items(), key=lambda x: x[1][1]))
                
        res = []
        end = -1
        for _, l in len_char:
            if l[0] > end:
                res.append(s[l[0]:l[1]+1])
                end = l[1]
        return res


    def maxNumOfSubstrings_2(self, s: str) -> list[str]:
        first = {c: s.find(c) for c in set(s)}
        last = {c: s.rfind(c) for c in set(s)}
        
        valid_intervals = []
        
        for c in set(s):
            start = first[c]
            end = last[c]
            
            is_valid = True
            i = start
            
            while i <= end:
                if first[s[i]] < start:
                    is_valid = False
                    break
                
                end = max(end, last[s[i]])
                i += 1
            
            if is_valid:
                valid_intervals.append((start, end))
                
        valid_intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        
        for start, end in valid_intervals:
            if start > prev_end:
                res.append(s[start:end+1])
                prev_end = end
                
        return res
        
a = Solution()
print(a.maxNumOfSubstrings("abaabbcaaabbbccd"))