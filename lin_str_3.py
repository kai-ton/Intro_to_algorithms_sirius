n = input().split()
st = []
for i in range(len(n)):
    if n[i] == '+':
        a = int(st[len(st) - 2]), int(st[len(st) - 1])
        st.pop()
        st.pop()
        st.append(a[0] + a[1])
    elif n[i] == '-':
        a = int(st[len(st) - 2]), int(st[len(st) - 1])
        st.pop()
        st.pop()
        st.append(a[0] - a[1])
    elif n[i] == '*':
        a = int(st[len(st) - 2]), int(st[len(st) - 1])
        st.pop()
        st.pop()
        st.append(a[0] * a[1])
    else:
        st.append(n[i])
print(*st)
