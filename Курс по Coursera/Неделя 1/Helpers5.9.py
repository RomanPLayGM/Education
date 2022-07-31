h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
time_1 = h1*60*60 + m1*60 + s1
# time_1 = time_1 % (24*60*60)
time_2 = h2 * 60 * 60 + m2*60 + s2
# time_2 = time_2 % (24*60*60)
print(time_2 - time_1)
