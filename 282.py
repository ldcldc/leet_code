class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def dfs(pointer, path, curr_val, prev_val):
            if pointer == len(num):
                if curr_val == target:
                    result.append(path)
                return
            
            for i in range(pointer + 1, len(num) + 1):
                curr_str = num[pointer:i]

                if len(curr_str) > 1 and curr_str[0] == '0':
                    break
                    
                curr_num = int(curr_str)
                
                if pointer == 0:
                    dfs(i, curr_str, curr_num, curr_num)
                else:
                    dfs(i, path + "+" + curr_str, curr_val + curr_num, curr_num)
                    dfs(i, path + "-" + curr_str, curr_val - curr_num, -curr_num)
                    dfs(i, path + "*" + curr_str, curr_val - prev_val + (prev_val * curr_num), prev_val * curr_num)

        dfs(0, "", 0, 0)
        return result
    
a = Solution()
print(a.addOperators('123456789',45))