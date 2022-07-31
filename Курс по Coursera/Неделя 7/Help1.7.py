def get_key(synonyms, word):
    for k, v in synonyms.items():
        if v == word:
            return k
        elif k == word:
            return v


n = int(input())
synonym = dict()
for i in range(n):
    words = input().split()
    Key = words[0]
    meaning = words[1]
    synonym[Key] = meaning
words = input()
print(get_key(synonym, words))
