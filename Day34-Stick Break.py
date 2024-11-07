t = int(input())
for i in range(0,t):
    L,K = map(int,input().split())
    if(L%K == 0):
        print("0")
    else:
        print("1")
