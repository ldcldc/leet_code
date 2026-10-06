from functools import cache

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        res = set()
        def dfs(str):
            right = str.find('}')
            if right == -1:
                res.add(str)
                return;
            
            left = str[:right].rfind('{')
            
            temp = str[left+1:right].split(',')
            
            for c in temp:
                dfs(str[:left] + c + str[right+1:])
                
        dfs(expression)
        
        return sorted(res)

    def braceExpansionII_2(self, expression: str) -> list[str]:
        
        @cache
        def dfs(s: str) -> set:
            right = s.find('}')
            if right == -1:
                return {s}
            
            left = s[:right].rfind('{')
            temp = s[left+1:right].split(',')
            
            res = set()
            for c in temp:
                res |= dfs(s[:left] + c + s[right+1:])
                
            return res
            
        return sorted(dfs(expression))
    
    
    
    def braceExpansionII_3(self, expression: str) -> list[str]:
        stack = []
        union_set = set()   # (+) ,로 연결될 단어 집합
        concat_set = {""}   # (*)
        
        for c in expression:
            if c == '{':       # 괄호만나면 스택에 싹다 백업
                stack.append((union_set, concat_set))
                union_set, concat_set = set(), {""}
                
            elif c == '}':
                union_set.update(concat_set)                # {} 안쪽 add
                prev_union, prev_concat = stack.pop()       # 스택 복구
                
                concat_set = set(j + i for j in prev_concat for i in union_set)
                
                union_set = prev_union
                
            elif c == ',':
                union_set.update(concat_set)
                concat_set = {""}
                
            else: # 알파벳
                concat_set = set(i + c for i in concat_set)
                
        union_set.update(concat_set)
        
        return sorted(union_set)
        
a = Solution()
print(a.braceExpansionII("{{a,z},a{a,c},{ab,z}}"))