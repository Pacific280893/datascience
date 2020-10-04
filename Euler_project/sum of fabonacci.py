import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    count=2
    a,b =1,2
    c =0
    while((a+b)<=n):
        c = a+b
        if(c%2==0 and c<=n):
            count+=c
        a=b
        b=c

    print(count)
