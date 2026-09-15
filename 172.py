def trailingZeroes(n):
    five = 5
    result = 0
    while five <= n:
        result += n//five
        five *= 5
    return result

def trailingZeroes_2(n):
    result = 0
    while 5 <= n:
        result += n//5
        n //= 5
    return result



print(trailingZeroes_2(25))