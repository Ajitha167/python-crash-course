n = int(input())
product = 1

while n > 0:
  digit = n % 10
  n = n//10
  product = product * digit
print(product)  
  
