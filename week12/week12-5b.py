a = 1500000000 #把數字便很大，變成10億 老大
b = 2000000000 #把數字變很大，變成20億 老二

c = a%b #老三
print(a, b, c)
while c!=0: #輾轉相除法
  a = b #老大變老二
  b = c #老二變老大
  c = a%b #老三變老二
  print(a, b, c) #新的老三算出來
print(b)