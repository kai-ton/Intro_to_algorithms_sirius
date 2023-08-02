m = int(input())
state_votes = {}
votes = {}
itog = {}
for _ in range(m):
    n = input().split()
    state_votes[n[0]] = n[1]
    votes[n[0]] = {}
m = int(input())
for _ in range(m):
    n = input().split()
    votes[n[0]][n[1]] = votes.get(n[0], {}).get(n[1], 0) + 1
    itog[n[1]] = 0
# print(votes)
for key, val in state_votes.items():
    m = ['', -999]
    for keys, vals in votes[key].items():
        if vals > m[1] or (vals == m[1] and keys < m[0]):
            m[0] = keys
            m[1] = vals
    itog[m[0]] = itog.get(m[0], 0) + int(val)
    # print(itog)
itog = sorted(itog.items(), key=lambda item: (-item[1], item[0]))
for i in range(len(itog)):
    print(*itog[i])
