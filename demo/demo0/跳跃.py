# 使用者：姜海波
# 创建时间：2023/3/25  11:28
n, m = map(int, input().split())
dp = [[*map(int, input().split())] for _ in range(n)]
direct = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (3, 0)]
for x in range(n):
    for y in range(m):
        res = []
        for dx, dy in direct:
            lx = x - dx
            ly = y - dy
            if 0 <= lx < n and 0 <= ly < m:
                res.append(dp[lx][ly])
        dp[x][y] += max(res) if len(res) != 0 else 0

print(dp[-1][-1])
