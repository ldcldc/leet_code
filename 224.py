def calculate(s):
    stack_num = ['/']
    stack_sign = []
    s = s.replace(" ","")
    s += '+0'
    for i, c in enumerate(s):
        if c.isdigit():
            stack_num.append(c)
        else :
            temp = ''
            while(stack_num[-1] != '/'):
                temp = stack_num.pop() + temp
                
            stack_num.pop()         # / 제거
            if temp:
                stack_num.append(temp)

            if c != '(':
                if stack_sign and stack_sign[-1] != '(':
                    sign = stack_sign.pop()
                    
                    if sign == '+':
                        stack_num.append(str(int(stack_num.pop())+int(stack_num.pop())))
                    if sign == '-':
                        stack_num.append(str(-int(stack_num.pop())+int(stack_num.pop())))
                    
            if c == ')':
                stack_sign.pop()     # ( 제거
            elif c == '-':
                if s[i-1] == '(' or i == 0:
                    stack_num.append('0')
                stack_sign.append(c)
            else:
                stack_sign.append(c)
            stack_num.append('/')
            
    return int(stack_num[0])


def calculate_2(s: str) -> int:
    stack = []
    curr_num = 0
    result = 0
    sign = 1            # curr_num의 부호
    
    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c in '+-':
            result += sign * curr_num
            curr_num = 0
            sign == 1 if c == '+' else sign == -1
        elif c == '(':
            stack.append(result)
            stack.append(sign)
            
            result = 0
            sign = 1
        elif c == ')':
            result += sign * curr_num
            curr_num = 0
            result = stack.pop()*result + stack.pop()
            
    result += sign * curr_num
    return result
            
print(calculate("1-( -2)"))