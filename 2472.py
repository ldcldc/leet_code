class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        interval = []
        for i in range(k - 1, len(s)):
            count = 0
            for j in range(i-k+1,i-k-1,-1):
                if s[j:i+1] == s[i:j-1:-1] if j > 0 else s[:i+1] == s[i::-1]:
                    interval.append((j,i))
                    break

        # interval = sorted(interval, key=lambda x:x[1])
        if not interval:
            return 0
        
        end = interval[0][1]
        count = 1
        for st, e in interval:
            if st > end:
                end = e
                count += 1
        return count

    def maxPalindromes_2(self, s: str, k: int) -> int:
        end = -1
        count = 0
        
        for i in range(k - 1, len(s)):
            for j in range(i-k+1, i-k-1, -1):
                if j < 0 or j <= end:
                    continue
                sub = s[j:i+1]
                if sub == sub[::-1]:
                    end = i
                    count += 1
                    break
        return count


a = Solution()
print(a.maxPalindromes("fttfjofpnpfydwdwdnns",2))