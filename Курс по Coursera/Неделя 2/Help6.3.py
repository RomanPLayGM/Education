l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
if l1 <= r2 and l2 <= r1 and l2 <= r3 and l3 <= r2:
    print(0)
elif l1 <= r3 and l3 <= r1 and l2 <= r3 and l3 <= r2:
    print(0)
elif l1 <= r3 and l3 <= r1 and l1 <= r2 and l2 <= r1:
    print(0)
elif l2 <= r3 and r2 >= l3:
    print(1)
elif l3 > r2 and ((r1 - l1) + r2 >= l3):
    print(1)
elif l2 > r3 and ((r1 - l1) + r3 >= l2):
    print(1)
elif l1 <= r3 and r1 >= l3:
    print(2)
elif l3 > r1 and ((r2 - l2) + r1 >= l3):
    print(2)
elif l1 > r3 and ((r2 - l2) + r3 >= l1):
    print(2)
elif l1 <= r2 and r1 >= l2:
    print(3)
elif l2 > r1 and ((r3 - l3) + r1 >= l2):
    print(3)
elif l1 > r2 and ((r3 - l3) + r2 >= l1):
    print(3)
else:
    print(-1)
