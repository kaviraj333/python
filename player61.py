amu,abi=map(int,raw_input().split())
l=raw_input().split()
k=0
for x in range(0,len(l)):
    c=0
    if(x==len(l)-1):
        c=int(l[0])+int(l[x])
    else:
        c=int(l[x])+int(l[x+1])
    if(c==abi):
        k=k+1
if(k>0):
    print("yes")
else:
    print("no")
