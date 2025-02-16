# DFS를 통해 조각 찾기
def find_block(board, f):
    L = len(board)    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def DFS(x, y, f, piece):
        visited[x][y] = True
        piece.append((x, y))

        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if L > nx >= 0 and L > ny >= 0:
                if not visited[nx][ny] and board[nx][ny] == f:
                    DFS(nx, ny, f, piece)
    
    pieces = []
    visited = [[False] * L for _ in range(L)]
    for i in range(L):
        for j in range(L):
            if not visited[i][j] and board[i][j] == f:
                piece = []
                DFS(i, j, f, piece)
                pieces.append(piece)
                
    return make_table(pieces)


# 찾아낸 퍼즐 조각을 2차원 리스트로 만들기
def make_table(pieces):
    tables = []
    for piece in pieces:
        x, y = zip(*piece)
        min_x, max_x = min(x), max(x)
        min_y, max_y = min(y), max(y)
        
        w = (max_y - min_y) + 1
        h = (max_x - min_x) + 1
        
        table = [[0] * w for _ in range(h)]
        for i, j in piece:
            table[i-min_x][j-min_y] = 1
        tables.append(table)
    
    return tables


# 퍼즐 조각을 회전시키기
def rotate(piece):
    rotated_pieces = []
    for i in range(4):
        rotated_piece = [[0] * len(piece) for _ in range(len(piece[0]))]
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                rotated_piece[j][len(piece)-i-1] = piece[i][j]
        rotated_pieces.append(rotated_piece)
        piece = rotated_piece
    
    return rotated_pieces


# 퍼즐 조각의 크기 구하기
def count_one(piece):
    cnt = 0
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1: cnt += 1
    return cnt


def solution(game_board, table):
    answer = 0
    
    empty_blocks = find_block(game_board, 0)
    puzzles = find_block(table, 1)
    
    for block in empty_blocks:
        is_filled = False
        
        for puzzle in puzzles:
            puzzle_cnt = count_one(puzzle)
            rotated_puzzles = rotate(puzzle)
            
            for rp in rotated_puzzles:
                if block == rp:
                    answer += puzzle_cnt
                    puzzles.remove(puzzle)
                    is_filled = True
                    break
                    
            if is_filled:
                break

    return answer