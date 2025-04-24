#k
n=7
mid = n//2
for i in range(n):
    for j in range(n):
        if  j== mid-1 or ((i+j == n-1) and i <= mid) or ((i == j) and i >= mid):
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()  

print()


#m
n=7
mid = n//2
for i in range(n):
    for j in range(n):
        if j == 0  or j == n-1  or (i==j and i <= mid) or (i+j == n-1 and i <= mid ):
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()  

#alternate 0 and 1
print()
start = 0
for i in range(n):
    for j in range(i+1):
        if start == 0:
            print(start,end=" ")
            start = 1
        else:
            print(start,end = " ")
            start = 0
    print()    

#another pattern:
for i in range(n):
    if i % 2 == 0:
            start = 0
    else:
            start = 1
    for j in range(i+1):
            print(start,end = " ")
            if start == 0:
                start = 1
            else:
                start = 0
    print()            

