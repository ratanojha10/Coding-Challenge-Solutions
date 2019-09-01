s=input("Enter String: ")
size=len(s)
w=0
res="False"
for i in range(size):
    try:
        k=10-int(s[i])
        for j in range(i,size):
            if s[j]==str(k):
                for x in s[i:j]:
                    if x=='?':
                        w+=1
                        
    except:
        continue

if w==3:
    print("True")
else:
    print("False")

