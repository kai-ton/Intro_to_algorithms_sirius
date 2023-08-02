st = []
while True:
    n = input()
    if 'push' in n:
        st.append(n.split()[1])
        print('ok')
    elif n == 'pop':
        if st != []:
            print(st[-1])
            st.pop()
        else:
            print('error')
    elif n == 'back':
        if st != []:
            print(st[-1])
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
