ra = [1,2,3,1,0]

def candy(ratings):
    l = len(ratings)
    candy = [1]*l
    
    for i in range(1,l):
        if ratings[i] > ratings[i-1]:
            candy[i] = candy[i-1] + 1
                    
    for i in range(l-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            candy[i] = max(candy[i+1] + 1, candy[i])
    
    return sum(candy)


def candy_2(ratings):
    """
    사탕 개수만 필요한 것이라면 ratings가 정확히 얼마인지는 필요x
    올라갔는지 내려갔는지만 알면 된다
    올라가면 이전거+1, 같으면 1,
    줄어들어도 1부터 +1로 계산
    ex) ratings = 1,2,2,3,4,5,4,3
      실제 candy = 1,2,1,2,3,4,2,1
                = 1,2,1,2,3,4,1,2
    줄어들 때 실제는 2,1을 받지만 1,2을 받는다고 해도 합은 같다.
    
    올라간 회수를 세다가 직후에 내려간 회수와 같아지는 순간부터 꼭대기에 하나를 더 주면 된다.
    ex) ratings = 2,3,4,5,4,3,2,1
      실제 candy = 1,2,3,5,4,3,2,1
                = 1,2,3,4,1,2,3,4 peak <= down
                       +1
    """
    
    l = len(ratings)
    
    sum_candy = 1
    
    up = 1
    down = 0
    peak = 1
    
    for i in range(1,l):
        if ratings[i] > ratings[i-1]:
            up += 1
            down = 0
            peak = up
            
            sum_candy += up
            
        elif ratings[i] == ratings[i-1]:
            up = 1
            down = 0
            peak = 1
            sum_candy +=1
            
        else :      #ratings[i] < ratings[i-1]
            up = 1
            down += 1
            
            sum_candy += down
            
            if peak <= down:
                sum_candy +=1
    return sum_candy

print(candy(ra))
print(candy_2(ra))
