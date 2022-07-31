import binascii
import json
f = open('hexes.txt').read()
print(len(f))
k = 0
g = []
for k in range(0, 10000):
    for i in range((749 * k), (749 * k) + 748):
        g.append(f[i])
# Перед вами 10000 записей одной длины, 9999 из них случайны, одно - флаг, зашифрованный однобайтовым ксором. hexes
#s = "".join(g)
#nums = binascii.unhexlify(s)
#strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
#y1 = max(strings, key=lambda s: s.count(' '))
#with open('result1.txt', 'w') as fw:
    #json.dump(y1, fw)
s = "".join(g)
nums = binascii.unhexlify(s)
key = max(nums, key=nums.count) ^ ord(' ')
y2 = ''.join(chr(num ^ key) for num in nums)
with open('result2.txt', 'w') as fw:
    json.dump(y2, fw)