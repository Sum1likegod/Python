def perm(fact,r,n):
  if r==0:
    return 1
  else:
    return fact(n)/(fact(n-r))

s=1
fact = lambda n : s*n
n = int(input("Enter the value of n "))
r = int(input("Enter the value of r "))
print(perm(fact,r,n))

sq = lambda x : x*x        
print(sq(5))      

