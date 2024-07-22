
def zoj(n):
    sum=0
    if n%2==0:
        return True
    else:
        return False
sum=0
fr=1
sc=2
while fr<4*10**6:
    if zoj(fr):
        #print(fr)
        sum=sum+fr
    new=fr+sc
    fr=sc
    sc=new
print(sum)
