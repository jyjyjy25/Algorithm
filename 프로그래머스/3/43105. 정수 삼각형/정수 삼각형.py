def solution(triangle):
    for i in range (1, len(triangle)):
        for j in range (len(triangle[i])):
            if i-1 >= 0 and j != 0 and j != len(triangle[i-1]):
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i-1]):
                triangle[i][j] += triangle[i-1][j-1]
    
    return max(triangle[-1])