n=int(input())
a=n//1000
b=n%1000//100
c=n%100//10
d=n%10
if b==c and a==d:
    print('YES')
else:
    print('NO')