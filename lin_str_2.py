a = list(input())
n = []
for i in range(len(a)):
    if a[i] == '(' or a[i] == '[' or a[i] == '{':
        n.append(a[i])
    else:
        if n == []:
            print('no')
            break
        if a[i] == ')' and n[-1] == '(':
            n.pop()
        elif a[i] == ']' and n[-1] == '[':
            n.pop()
        elif a[i] == '}' and n[-1] == '{':
            n.pop()
        else:
            print('no')
            break
else:
    if n == []:
        print('yes')
    else:
        print('no')
