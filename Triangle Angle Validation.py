a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180 and a > 0 and b > 0 and c > 0:
  print("VALID")
  if a == b == c == 60:
    print("EQUILATERAL")
  elif a==b or a==c  or b==c:
    print("ISOSCELES")
  else:
    print("SCALENE")
else:
  print("NOT VALID")
    
    
