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

def encryp(r,c):
    fstg=''
    k=0
    for i in range(r):
        for j in range(c):
            if k<=(size-1):
                print(nstg[k],end='')
                k+=1
            else:
                pass
        print() 
    for x in range(c):
        m=0
        for y in range(r):
            if (m+x)<=(size-1):
                fstg+=nstg[m+x]
                m+=c
        fstg+=' '
    print(fstg)

if row*col>size:
    encryp(row,col)
else:
    encryp(row+1,col)
