# 使用者：姜海波
# 创建时间：2022/12/20  0:02
list1 = [[0] * 100] * 100
row = 0
col = 0
cnt = 1
list1[0][0] = 1
while list1[19][19] == 0:
    # 右移
    col += 1
    cnt += 1
    list1[row][col] = cnt
    while col:
        row += 1
        col -= 1
        cnt += 1
        list1[row][col] = cnt
    row += 1
    cnt += 1
    list1[row][col] = cnt
    while row:
        row -= 1
        col += 1
        cnt += 1
        list1[row][col] = cnt
print(list1[19][19])
