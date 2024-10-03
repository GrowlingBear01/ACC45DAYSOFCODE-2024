t=int(input("Enter no of cases:-"))
while t>0:
    X,Y=map(int,input("Enter no of minutes for each question\n").split())
    A=(500-X*2)+(1000-(X+Y)*4)
    B=(1000-Y*4)+(500-(X+Y)*2)
    print(max(A,B))
    t-=1
    
