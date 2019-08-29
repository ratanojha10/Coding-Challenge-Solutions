#Error

num=int(input("Input test cases: "))

for i in range(num):
    stg=input("Enter String: ")
    B=0
    A="False"
    size=len(stg)
    for i in range(size):
        try:
            for j in range(size):
                if int(stg[j])+int(stg[i])==10:
                    for x in range(i,j+1,1):
                        if stg[x]=='?':
                            B+=1
                            continue
                        else:
                            continue
                            
                else:
                    continue
                               

        except:
            continue
    if B==3:
        A="True"
    print(B)

