st = []
while True:
    n = input()
    if 'push' in n:
        st.append(n.split()[1])
        print('ok')
    elif n == 'pop':
        if st != []:
            print(st[0])
            st.pop(0)
        else:
            print('error')
    elif n == 'front':
        if st != []:
            print(st[0])
        else:
            print('error')
    elif n == 'size':
        print(len(st))
    elif n == 'clear':
        st = []
        print('ok')
    elif n == 'exit':
        print('bye')
        break
