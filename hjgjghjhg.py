import binascii
import json
f = open('hexes.txt').read()
print(len(f))
a = ['"', ' ']
f5 = r"\0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_}{-',?!#$.><:|/[];^&*()=+`~@№%абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
for i in f5:
    a.append(i)
print(a)
with open("hexes.txt") as myfile:
    data = "".join(line.rstrip() for line in myfile)
nums = binascii.unhexlify(data)
strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
f4 = str(max(strings, key=lambda s: s.count(' ')))
a2 = []
for i in f4:
    a2.append(i)
with open('tytg.txt', 'w') as fw:
    json.dump(a2, fw)
a1 = []
for i in f4:
    for j in a:
        if i == j:
            a1.append(i)
        elif i == '\\':
            print(i)
with open('yuityutyu.txt', 'w') as fw:
    json.dump(a1, fw)
# yoXTDc3f_NM0Mig6LAobbeudRLP0NHXRPSY
# y?oXTDc!3f_N$M0Mig6LAobb#eudRLP0N?HXRP!.SY
# (y?o\"XT>Dc!3`f_N$+M0Mig6LAob;b#e]udRLP>0N?HXRP!.S+Y\"
# (y?o\"XT>Dc!3`f_N$+M0\\Mig6LAob;b#e]udRLP\\>0N?HXRP!.S+Y\"
# (y?o\"XT>Dc!3`f@_N$+M0\\Mig6LAob;b#e]udRLP\\>0N?HXRP!.S+Y\"
# C", "C", "{", "y", "o", "X", "T", "D", "c", "3", "f", "_", "N", "M", "0", "M", "i", "g", "6", "L", "A", "o", "b", "b", "e", "u", "d", "R", "L", "P", "0", "N", "H", "X", "R", "P", "S", "Y", "}",
# "C", "C", "{", "y", "?", "o", "X", "T", "D", "c", "!", "3", "f", "_", "N", "$", "M", "0", "M", "i", "g", "6", "L", "A", "o", "b", "b", "#", "e", "u", "d", "R", "L", "P", "0", "N", "?", "H", "X", "R", "P", "!", ".", "S", "Y", "}"
# "C", "C", "{", "(", "y", "?", "o", "\"", "X", "T", ">", "D", "c", "!", "3", "`", "f", "_", "N", "$", "+", "M", "0", "M", "i", "g", "6", "L", "A", "o", "b", ";", "b", "#", "e", "]", "u", "d", "R", "L", "P", ">", "0", "N", "?", "H", "X", "R", "P", "!", ".", "S", "+", "Y", "\"", "}"
# "(", "y", "?", "o", "\"", "X", "T", ">", "D", "c", "!", "3", "`", "f", "_", "N", "$", "+", "M", "0", "\\", "M", "i", "g", "6", "L", "A", "o", "b", ";", "b", "#", "e", "]", "u", "d", "R", "L", "P", "\\", ">", "0", "N", "?", "H", "X", "R", "P", "!", ".", "S", "+", "Y", "\"", "}"
# "C", "C", "{", "(", "y", "?", "o", "\"", "X", "T", ">", "D", "c", "!", "3", "`", "f", "@", "_", "N", "$", "+", "M", "0", "\\", "M", "i", "g", "6", "L", "A", "o", "b", ";", "b", "#", "e", "]", "u", "d", "R", "L", "P", "\\", ">", "0", "N", "?", "H", "X", "R", "P", "!", ".", "S", "+", "Y", "\"", "}"