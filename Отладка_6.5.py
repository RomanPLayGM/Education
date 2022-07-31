import random

a = []
place = ['l', 'r']
for i in range(100):
    in_ = random.randint(0, 990)
    out_ = random.randint(in_, 1000)
    in_place = random.choice(place)
    out_place = random.choice(place)
    res = f"{in_} {out_} {in_place} {out_place}"
    a.append(res)
    print(res)
