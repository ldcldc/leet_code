from bisect import bisect_right, bisect_left

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        result = 0
        length = len(str(n))
        num_digit = len(digits)
        for i in range(1,length):
            result += num_digit**i
            
        if str(n)[0] < digits[0]:
            return result
            
        for i in range(length):
            if str(n)[i] < digits[0]:
                return result
            elif str(n)[i] == digits[-1]:
                result += (num_digit-1) * (num_digit ** (length - i - 1))
            elif str(n)[i] > digits[-1]:
                result += num_digit ** (length - i)
                return result
            else:
                index = bisect_right(digits, str(n)[i]) - 1 
                if digits[index] == str(n)[i]:
                    result += index * (num_digit ** (length - i - 1))
                if digits[index] < str(n)[i]:
                    result += (index + 1) * (num_digit ** (length - i - 1))
                    return result
        return result + 1 if str(n)[-1] in digits else result

    def atMostNGivenDigitSet_2(self, digits: List[str], n: int) -> int:
        S = str(n)
        len_n = len(S)
        len_d = len(digits)
        
        result = 0
        
        for i in range(1, len_n):
            result += len_d ** i
            
        for i, char in enumerate(S):
            index = bisect_left(digits, char)
            result += index * (len_d ** (len_n - 1 - i))
            
            if index < len_d and digits[index] == char:
                continue
            else:
                return result
                
        return result + 1
    
a = Solution()
print(a.atMostNGivenDigitSet(["3","4","6","7","9"],4170))