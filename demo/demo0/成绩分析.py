# 使用者：姜海波
# 创建时间：2022/12/8  22:23
num = int(input())
maxnum = 0
minnum = 100
total = 0
for i in range(num):
    a = int(input())
    maxnum = max(maxnum, a)
    minnum = min(minnum, a)
    total += a

print(maxnum)
print(minnum)
# print(round(total / num, 2))
print(f'{total/num:.2f}')