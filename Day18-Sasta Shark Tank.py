T=int(input())

for _ in range((T)):
    A,B=map(int,input().split())
    
    if A/0.1>B/0.2:
        print("FIRST")
    elif A/0.1==B/0.2:
        print("ANY")
    else:
        print("SECOND")
