n = int(input())
summ = 0
for i in range(1,(n//2)+1):
    if n % i == 0:
      summ = summ + i
if summ == n:
  print("Perfect")
else:
  print("Not Perfect")
  
