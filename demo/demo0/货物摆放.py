# 使用者：姜海波
# 创建时间：2023/3/18  22:11
import math
n=2021041820210418
m=int(pow(n,1/2)+1)
lis=[]
ans=0
for i in range(1,m):
    if n%i==0:
        lis.append(i)
        if n/i!=i:
            lis.append(n/i)
for i in lis:
    for j in lis:
        for k in lis:
            if (i*j*k==n):
                ans+=1
print(ans)

