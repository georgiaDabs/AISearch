import re
file_object=open("AISearchtestcase.txt","r")
fileText=file_object.read()
print(fileText)
y=[int(s) for s in re.findall(r'-?[0-9]+',fileText)]
n=y.pop(0)
print(y)
m=n-1
a=[[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        #print(str(y[0]) +"is put in place ("+str(i)+","+str(j)+")")
        a[i][j]=y.pop(0)
        a[j][i]=a[i][j]
for row in a:
    print(row)
