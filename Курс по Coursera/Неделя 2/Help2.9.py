l1, h1, w1 = int(input()), int(input()), int(input())
l2, h2, w2 = int(input()), int(input()), int(input())
a = (l1//l2) * (h1//h2) * (w1//w2)
b = (l1//l2) * (h1//w2) * (w1//h2)
c = (l1//h2) * (h1//l2) * (w1//w2)
a1 = (l1//h2) * (h1//w2) * (w1//l2)
b1 = (l1//w2) * (h1//l2) * (w1//h2)
c1 = (l1//w2) * (h1//h2) * (w1//l2)
m = a
if m < b:
    m = b
if m < c:
    m = c
if m < a1:
    m = a1
if m < b1:
    m = b1
if m < c1:
    m = c1
print(m)
