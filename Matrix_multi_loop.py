n1,m1=map(int,input("Enter The size of first matrix : n m : ").split())
X=[]
for i in range(n1):
    temp=list(map(int,input().split()))
    X.append(temp)

n2,m2=map(int,input("Enter The size of second matrix : n m : ").split())
Y=[]
for i in range(n2):
    temp=list(map(int,input().split()))
    Y.append(temp)
    result=[]
for i in range(m1):
    temp=[]
for j in range(n2):
    temp.append(0)
    result.append(temp)


# iterate through rows of X
for i in range(n1):
# iterate through columns of Y
    for j in range(n2):
# iterate through rows of Y
        for k in range(m1):
            result[i][j] += X[i][k] * Y[k][j]
            for r in result:
                print(r)