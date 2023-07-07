import random
a = ['a','b','c','d']
for i in range (len(a)):
    for j in range(9):
        print(a[i])
        print(j)
        if j==5:
            m=random.randint(1,2)
            if m ==1:
                print(m)
                break