import sys

x = 1
y = 3
for i in range(x, 8):
    for j in range(y,8):
        if i-x == j-y:
            print(i, j)
for i in range(x, -1, -1):
    for j in range(y,-1,-1):
        if i-x == j-y:
            print(i, j)


i = x
j = y
while i < 8 and j < 8:
    print(i,j)
    i += 1
    j += 1
    if[i, j] == [4,6]:
        break

i = x
j = y
while i > -1 and j > -1:
    print(i,j)
    i -= 1
    j -= 1