for t in range(int(input())):
    n = int(input())
    sum = 0.0
    if n%2==0:
      for i in range(2,n+1,2):
         sum += 1.0/i
    else:
       for i in range(1,n+1,2):
          sum += 1.0/i
    print(f"{sum:.6f}")