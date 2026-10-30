n = int(input())

if n % 3==0 and n% 5!=0:
  print("Thala")
elif n % 5==0 and n % 3!=0:
  print("Thalapathy")
elif n % 3==0 and n % 5==0:
  print("ThalaThalapathy")
else:
  print(n)
