n = int(input())
st_1 = list(reversed(list(map(int, input().split()))))
st_t = []
for i in range(n):
    if st_t != [] and st_t[-1] == i + 1:
        st_t.pop()
    else:
        m = 0
        j = 0
        while st_1 != []:
            if st_1[-1] == i + 1:
                st_1.pop()
                m = 1
                break
            else:
                st_t.append(st_1[-1])
                st_1.pop()
        if m == 0:
            print('NO')
            break
    # print(st_1)
    # print(st_t)
else:
    print('YES')
