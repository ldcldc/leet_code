from collections import Counter
import math

p = [[-6,-1],[3,1],[12,3]]

def maxPoints(points):
    if len(points) <= 2:
        return len(points)
    
    slope = Counter()
    for i in range(len(points)):        #[0],[1]
        for j in range(i+1,len(points)):
            print((points[i][0],points[i][1]), (points[j][0],points[j][1]))
            if points[i][0] == points[j][0]:
                a = 'x'
                b = points[i][0]
            else:
                a = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                b = round(points[i][1] - a*points[i][0]) #어차피 모든 점이 정수이므로 같은 기울기 안에서는 1 이상 차이남
            slope[(a, b)] += 1
    return ((1 + math.isqrt(1 + 8 * slope.most_common(1)[0][1])) // 2)

def maxPoints_2(points):
    
    if len(points) <= 2:
        return len(points)
        
    global_max = 0
    
    
    for i in range(len(points)):
        slope = Counter()
        for j in range(i+1,len(points)):
            a = 'x' if points[i][0] - points[j][0] == 0 else \
                (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) 
            slope[a] += 1
        if slope:
            global_max = max(global_max, max(slope.values()))
    return global_max+1
            
print(maxPoints_2(p))