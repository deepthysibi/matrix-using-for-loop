


# create a matrix in for loop by reading elements by user and print its transpose:
l=[]
rows=int(input("enter the no.of rows: "))
column = int(input("enter the no.of columns: "))
for r in range(rows):
    a=[]
    for c in range(column):
        e=int(input("enter the element: "))
        a.append(e)
    l.append(a)
print(l)
for r in range(rows):
    for c in range(column):
        print(l[r][c],end=" ")
    print()
for c in range(column):
    for r in range(rows):
        print(l[r][c],end=" ")
    print()