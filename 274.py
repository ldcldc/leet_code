c= [3,0,6,1,5]

def hIndex(citations):
    
    n = len(citations)
    
    if not n:
        return 0
    
    max_ci = max(citations)
    
    if not max_ci:
        return 0
    citations_number = [0] * max(max_ci)

    for i in range(n):
        for j in range(citations[i]):
            citations_number[j] += 1

    print(citations_number)
                
    for i in range(len(citations_number)):
        print(f'i = {i}')
        if i+1 <= citations_number[i]:
            h_index = i
            print(f'h_index = {h_index}')
            
    return h_index+1


def hIndex_2(citations):
    n = len(citations)
    
    citations_number = [0] * (n+1)
    sum = 0
    
    for i in citations:
        if i > n:
            citations_number[n] += 1
        else:
            citations_number[i] += 1
    # print(citations_number)
    
    for i in range(n, -1, -1):
        sum += citations_number[i]
        if i <= sum:
            return i

print(hIndex_2(c))