t = int(input("Enter number of test cases: \n"))
while t > 0:
    Xa,Xb,Xc = map(int,input("Enter number of votes for each party-").split())
    if Xa + Xb + Xc <= 101:
        if Xa > Xb and Xa > Xc:
            print("Party A won by", Xa, "votes.")
        elif Xb > Xa and Xb > Xc:
            print("Party B won by", Xb, "votes.")
        elif Xc > Xa and Xc > Xb:
            print("Party C won by", Xc, "votes.")
        else:
            print("It's a tie!")
    else:
        print("NOTA")
    
    t -= 1
