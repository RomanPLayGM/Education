a, b, c = map(int, input().split())
const = 0
const1 = 0
if a > b:
    const = a - b
else:
    const = b - a
if a > b:
    if c > 0:
        const1 = (a + c) - b
    else:
        if a + c > b:
            const1 = (a + c) - b
        else:
            const1 = b - (a + c)
else:
    if c > 0:
        if a + c > b:
            if a > 0:
                if c > b:
                    const1 = c - b
            else:
                if c > b:
                    const1 = (a + c) - b
        else:
            const1 = b - (a + c)
    else:
        const1 = b - (a + c)

print(min(const1, const))
