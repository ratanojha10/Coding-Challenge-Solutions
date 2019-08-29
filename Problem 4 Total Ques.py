#Error


num=int(input("Input test cases: "))

for i in range(num):
    stg=input("Enter String: ")
    if '???' in stg:
        for j in range(len(stg)):
            if stg[j]=='?':
                if stg[j+1]=='?' and stg[j+2]=='?':
                    try:
                        if int(stg[j-1])+int(stg[j+3])==10:
                            print("True")
                            break
                    except:
                        print("False")
    elif '???' not in stg:
        print("True")


