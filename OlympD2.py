a, b, c = map(int, input().split())
const = 0
const1 = 0
print(min(abs(a - b), abs(c - abs(a - b))))
if a >= 0 and b >= 0:
    for i in range(a, b):
        const1 += 1
    if a == b:
        const = 0
    else:
        if (a + c) < b:
            a += 1
            const += 1
            if (a + c) < b:
                a += c
                if a < b:
                    for i in range(a, b):
                        a += 1
                        const += 1
        else:
            a += c
            if a > b:
                for j in range(b, a):
                    a -= 1
                    const += 1
    print(min(const1, const))
elif ((a < 0) and (b >= 0)):
    for i in range(a, b):
        const1 += 1
    if a == b:
        const = 0
    else:
        if (a + c) < b:
            a += 1
            const += 1
            if (a + c) < b:
                a += c
                if a < b:
                    for i in range(a, b):
                        a += 1
                        const += 1
        else:
            a += c
            if a > b:
                for j in range(b, a):
                    a -= 1
                    const += 1
    print(min(const1, const))
elif ((b < 0) and (a >= 0)):
    for i in range(b, a):
        const1 += 1
    if a == b:
        const = 0
    else:
        if (a + c) < b:
            a += 1
            const += 1
            if (a + c) < b:
                a += c
                if a < b:
                    for i in range(a, b):
                        a += 1
                        const += 1
        elif (a + c) == b:
            const = 0
        else:
            a += c
            if a > b:
                for j in range(b, a):
                    a -= 1
                    const += 1
    print(min(const1, const))
else:
    if a == b:
        const = 0
    else:
        if a > b:
            for i in range(b, a):
                const1 += 1
        else:
            for i in range(a, b):
                const1 += 1
        if a < b:
            if (a + c) < b:
                a += 1
                const += 1
                if (a + c) < b:
                    a += c
                    if a < b:
                        for i in range(a, b):
                            a += 1
                            const += 1
            else:
                a += c
                if a > b:
                    for j in range(b, a):
                        a -= 1
                        const += 1
        else:
            if (a + c) > b:
                a -= 1
                const += 1
                if (a + c) > b:
                    a += c
                    if a > b:
                        for i in range(b, a):
                            a -= 1
                            const += 1
            else:
                a += c
                if a < b:
                    for j in range(a, b):
                        a += 1
                        const += 1
    print(min(const1, const))