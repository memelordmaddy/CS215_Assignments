x=[]
y=[]
for j in range (1, 201):
    l=float(1)
    r=float(1)
    for i in range (1, j):
        l*= (200-i)/200
        r*=(199-i)/200
    op= l-r
    x.append(j)
    y.append(op)

max=0
max_index=0
for i in range (0, len(y)):
    if(y[i]> max):
        max= y[i]
        max_index=x[i]
print(max_index)