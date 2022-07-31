n = int(input())
set1 = set(input() for _ in range(int(input())))
set2 = set1.copy()
for j in range(1, n):
    setlan = set(input() for _ in range(int(input())))
    set1 |= setlan
    set2 &= setlan
for mno in [set2, set1]:
    print(len(mno), *mno, sep='\n')
