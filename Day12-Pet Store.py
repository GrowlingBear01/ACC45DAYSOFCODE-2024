for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    flag=0
    for i in s:
        if l.count(i)%2:
            flag=1
    if flag==1:
        print('NO')
    else:
        print('YES')
