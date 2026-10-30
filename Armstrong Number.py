n = int(input())

temp = n
digit = 0
while n > 0:
  n = n // 10
  digit+=1
n = temp
summ = 0 
while n > 0:
  last = n % 10
  summ = summ + (last**digit)
  n = n // 10
if summ == temp:
  print("Armstrong")
else:
  print("Not Armstrong")
