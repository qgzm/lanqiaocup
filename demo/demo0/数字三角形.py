# 使用者：姜海波
# 创建时间：2022/12/8  1:04
n = int(input())
w = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(0, i + 1):
        if j == 0:
            w[i][j] += w[i - 1][j]
        elif j == i:
            w[i][j] += w[i - 1][j - 1]
        else:  # 其余元素由上方较大值得到
            w[i][j] += max(w[i - 1][j - 1: j + 1])
if n & 1:  # 如果是奇数行，则返回最中间值
    print(w[-1][n // 2])
else:  # 偶数行则返回中间较大值
    print(max(w[-1][n // 2 - 1], w[-1][n // 2]))
