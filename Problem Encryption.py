stg=input("Enter string: ")
nstg=""
for i in stg:
    if i !=' ':
        nstg+=i
    else:
        continue

size=len(nstg)
row=int((size**0.5)//1)
col=int(((size**0.5)//1)+1)
if row*col>=size:
    fstg=''
    k=0
    for i in range(row):
        for j in range(col):
            if k<=(size-1):
                print(nstg[k],end='')
                k+=1
            else:
                pass
        print() 

    for x in range(col):
        m=0
        for y in range(row):
            if (m+x)<=(size-1):
                fstg+=nstg[m+x]
                m+=col
        fstg+=' '
    print(fstg)

else:
    row+=1
    fstg=''
    k=0
    for i in range(row):
        for j in range(col):
            if k<=(size-1):
                print(nstg[k],end='')
                k+=1
            else:
                pass
        print() 

    for x in range(col):
        m=0
        for y in range(row):
            if (m+x)<=(size-1):
                fstg+=nstg[m+x]
                m+=col
        fstg+=' '
    print(fstg)    
    
    
