d = []
while True:
    n = input()
    if 'push_front' in n:
        b, d = d, [n.split()[1]]
        d = [b] + d
        for i in range(len(b)):
            d.append(b[i])
        print('ok')
    elif 'push_back' in n:
        d.append(n.split()[1])
        print('ok')
    elif n == 'pop_front':
        if d != []:
            print(d[0])
            d.pop(0)
        else:
            print('error')
    elif n == 'pop_back':
        if d != []:
            print(d[-1])
            d.pop()
        else:
            print('error')
    elif n == 'front':
        if d != []:
            print(d[0])
        else:
            print('error')
    elif n == 'back':
        if d != []:
            print(d[-1])
        else:
            print('error')
    elif n == 'size':
        print(len(d))
    elif n == 'clear':
        d = []
        print('ok')
    elif n == 'exit':
        print('bye')
        break
