h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
print(t1)
t1 = t1 % (24*60*60)
print(t1)
t2 = h2*60*60 + m2*60 + s2
print(t2)
t2 = t2 % (24*60*60)
print(t2)
print(t2-t1)