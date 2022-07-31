fin = open('input.txt', 'r', encoding='utf-8')
text = fin.read().split()
print(len(set(text)))
