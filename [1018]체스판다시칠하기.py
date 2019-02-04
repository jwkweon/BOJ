import sys

M, N = map(int, input().split())
W, B = 'W', 'B'

board = []
for i in range(M):
    input_ = sys.stdin.readline()
    board.append(input_)

chess_w = [[W, B, W, B, W, B, W, B],
           [B, W, B, W, B, W, B, W],
           [W, B, W, B, W, B, W, B],
           [B, W, B, W, B, W, B, W],
           [W, B, W, B, W, B, W, B],
           [B, W, B, W, B, W, B, W],
           [W, B, W, B, W, B, W, B],
           [B, W, B, W, B, W, B, W]]
chess_b = [[B, W, B, W, B, W, B, W],
           [W, B, W, B, W, B, W, B],
           [B, W, B, W, B, W, B, W],
           [W, B, W, B, W, B, W, B],
           [B, W, B, W, B, W, B, W],
           [W, B, W, B, W, B, W, B],
           [B, W, B, W, B, W, B, W],
           [W, B, W, B, W, B, W, B]]

ans = []
for m in range(M - 7):
    for n in range(N - 7):
        ans1, ans2 = 0, 0
        for i in range(8):
            for j in range(8):
                if board[m + i][n + j] != chess_w[i][j]:
                    ans1 += 1
                if board[m + i][n + j] != chess_b[i][j]:
                    ans2 += 1
        ans.append(min(ans1, ans2))

print(min(ans))
