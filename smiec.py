a=' X X X | X X X | X X X\n X X X | X X X | X X X\n X X X | X X X | X X X\n - - - - - - - - - - -\n X X X | X X X | X X X\n X X X | X X X | X X X\n X X X | X X X | X X X\n - - - - - - - - - - -\n X X X | X X X | X X X\n X X X | X X X | X X X\n X X X | X X X | X X X '
print(a)
tab_wall_2=[]
tab_wall_1=[]
tab_spaces =[]
tab_n=[]
for i in range(len(a)):
    if a[i]=='-':
        tab_wall_2.append(i)
    elif a[i] == "|":
        tab_wall_1.append(i)
    elif a[i] == " ":
        tab_spaces.append(i)
    elif a[i] == "\n":
        tab_n.append(i)

"""print(tab_wall_1)
print(tab_wall_2)
print(tab_n)
print(tab_spaces)

a='cc'
b='X'
print(a+b)"""

[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]