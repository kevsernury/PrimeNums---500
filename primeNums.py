flag = 0
for i in range(500, 600):
    for j in range(2, i):
        if i % j == 0:
            flag = 0
            break
        else:
            flag = 1
    if flag:
        print (i)
