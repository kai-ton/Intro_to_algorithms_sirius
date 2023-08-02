a, b, d = map(int, input().split())
if (b - a) % 2 == 0:
    print(
        (b - a) // 2 + a,
        min(
            ((b - a) // 2 + a) % d,
            (d - ((b - a) // 2 + a)) % d
        )
    )
    # print(1)
else:
    if ((b - a) // 2 + a) % d >= (d - ((b - a) // 2 + a + 1)) % d:
        print((b - a) // 2 + a + 1, (d - ((b - a) // 2 + a + 1)) % d)
        # print(2)
    else:
        print((b - a) // 2 + a, ((b - a) // 2 + a) % d)
#         print(3)
# print(((b - a) // 2 + a) % d, d - ((b - a) // 2 + a) % d)
