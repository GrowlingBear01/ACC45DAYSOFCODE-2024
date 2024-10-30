for i in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    
    l=[]
    #sum of b
    s=sum(b)
    for i in range(n):
        l.append(b[i] - (s//(n+1)) )
        
    print(*l)
