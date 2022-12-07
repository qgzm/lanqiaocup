# 使用者：姜海波
# 创建时间：2022/10/21  18:58
import datetime

date = input()
y = int(date[0:4])
m = int(date[4:6])
d = int(date[6:])
dd = datetime.date(y, m, d)
# print(dd)
flag = True
for i in range(99999999):
    dd = dd + datetime.timedelta(days=1)
    # print(dd+datetime.timedelta(days=1))
    strdd = str(dd).replace('-', '')
    if strdd == strdd[::-1]:
        if flag:
            print(strdd)
            flag = False
    if strdd[0] == strdd[2] == strdd[-1] == strdd[-3] and strdd[1] == strdd[3] == strdd[-2] == strdd[-4]:
        print(strdd)
        break
# timedelta(days=,seconds=,months=) 在dd的基础上加时间
