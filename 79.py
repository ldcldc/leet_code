b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
w = "SEE"

def exist(board, word):
    m = len(board[0])   #j
    n = len(board)      #i
    new_board = [[[char, True] for char in row] for row in board]
    w_len = len(word)
    
    result = False
    
    def search(w, i, j):
        nonlocal result
        if w_len == w:                      #단어 완성시 result = True
            result = True
            return
        
        if not(0 <= i < n and 0 <= j <m):   #i,j가 보드 밖을 가리키면 return
            return
        if not new_board[i][j][1]:          # 이미 추가한 글자면 return
            return
            
        if word[w] == board[i][j]:          #해당 순서의 word와 일치하면 다음word찾으러
            new_board[i][j][1] = False      #온거 체크
            search(w + 1, i +1, j)          #상하좌우
            search(w + 1, i -1, j)
            search(w + 1, i, j +1)
            search(w + 1, i, j -1)
            new_board[i][j][1] = True
        return
        
        
    for i in range(n):
        for j in range(m):
            if word[0] == board[i][j]:  
                search(0, i, j)
    return result


def exist_2(board, word):
    m = len(board[0])   #j
    n = len(board)      #i
    w_len = len(word)
    
    def search(w, i, j):

        if w_len == w:                      #단어 완성시 result = True
            return True
        #i,j가 보드 밖을 가리키거나 이미 추가한 글자거나 word와 다른 글자면 return
        if not(0 <= i < n and 0 <= j <m and word[w] == board[i][j]):   
            return False
        
        temp,board[i][j] = board[i][j],'visit' #방문처리
        #하나라도 true나오면 바로 뒤 무시하고 result = true
        result = search(w + 1, i +1, j) or search(w + 1, i -1, j)\
            or search(w + 1, i, j +1) or search(w + 1, i, j -1)
            
        board[i][j] = temp
        
        return result
        
    for i in range(n):
        for j in range(m):
            if word[0] == board[i][j]:  
                if search(0, i, j):
                    return True
    return False
            
    
print(exist_2(b, w))

