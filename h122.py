amu=int(raw_input())
l1=raw_input().split()
l=[]
for x in l1:
    l.append(int(x))
for x in range(1,amu):
    k1=0
    k2=0
    j=x+1
    while(j<=amu-1):
        k1=k1+int(l[j])
        j+=1
    i=x-1
    while(i>=0):
        k2=k2+int(l[i])
        i-=1
    if(k1==k2):
        print("yes")
        break
else:
    print("no")
