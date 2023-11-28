#最大公因數(數字大跑很久) 
a = 100000000 #把數字便很大，變成10億
b = 200000000 #把數字變很大，變成20億
ans = 0
for i in range(1, a+1):
  if a%i==0 and b%i==0:
    print( i, '有整除' )
    ans = i
print(ans, '是最大公因數')