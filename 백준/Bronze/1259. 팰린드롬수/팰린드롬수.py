while(True):
    x = input()
    if (x == '0'):
        break

    check = True
    for i in range(len(x)//2):
        if (x[i] != x[-i-1]):
            check = False
            break
    
    if check:
        print('yes')
    else:
        print('no')