a = 120
# 1 2 3 4 5 6 10 12 ... for 迴圈
ans = 0
for i in range(1, a+1): #1l 包含本身
  if a%i==0:
    print( i, end=' ' )
    ans += 1 #迴圈裏面，增加
print('有幾個整除?', ans) #迴圈後面，把ans拿來用