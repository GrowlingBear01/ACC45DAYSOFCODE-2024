T=int(input("Enter no of cases\n"))

while T>0:
    N,K=map(int,input().split())
    for i in range(N):
        A=int(input("Amount need:-"))
        if A<=K:
            K=K-A
            print(K,"Amount left\n")
        else:
            print("No money left in ATM")
    T-=1
