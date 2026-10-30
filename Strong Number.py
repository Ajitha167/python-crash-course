n = int(input())
digit = n
temp = 0
while n > 0:
  last = n % 10
  total=1
  for i in range(1,last+1):
    total = total*i
  temp += total  
  n = n // 10
if digit == temp:
  print("Strong")
else:
  print("Not Strong")
  
  
  
