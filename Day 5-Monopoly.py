T=int(input("Enter no of test cases"))
while T>0:
    P,Q,R,S=map(int,input("Enter profit:-").split())
    if P>Q+R+S:
        print("yes")
    elif Q>P+R+S:
        print("yes")
    elif R>P+Q+S:
        print("yes")
    elif S>P+Q+R:
        print("yes")
    else:
        print("NO")
    T-=1
