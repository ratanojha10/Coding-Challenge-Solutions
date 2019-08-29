from itertools import permutations
case=int(input("Enter number of test cases: "))
for i in range(case):
    try:
        stg=input("Enter string: ")
        tup=tuple(stg)
        A=permutations(stg)
        k=[]
        nlst=None
        nstg=''
        for j in list(A):
            k+=[j]
        k.sort()
        for x in range(len(k)):
            if k[x]==tup:
                nlst=tuple(k[x+1])
        for y in nlst:
            nstg+=str(y)
        print(nstg)
    except:
        print("No answer")
        
