a = [0] #有100格，每隔都是0
a[0] = 1
a[1] = a
for i in range(2, 100):
  a[i] = a[i-1] + a[i-2]
print(a)
