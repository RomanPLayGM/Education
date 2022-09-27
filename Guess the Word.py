"""
Условие задачи:

Имеется некоторое непустое множество уникальных строк и некоторое секретное слово,
которое находится в этом множестве, представленное в виде непустой строки. Так ж
е на входе предоставлен некоторый сторонний интерфейс Master, метод которого будет возвращать к
оличество совпавших символов по соответствующим индексам между переданной строкой и секрет
ным словом. Если этого слова нет в списке, метод guess() интерфейса Master вернет -1. Необходимо
не больше чем за 10 вызовов метода Master.guess(const std::string& strToCompare) найти секретно
е слово из списка. Секретное слово считается найденным, если вы смогли вызвать метод guess() от вашег
о секретного слова.

Говоря формальным языком, необходимо реализовать функцию, которая не более чем за 10 попыток выз
овет метод guess() у Master секретным словом в качестве аргумента. То есть, наша задача больше зак
лючается в построении стратегии угадывания секретного слова.

Ограничения:

wordlist[i].length == 6

wordlist[i] из множества ['a', 'b'...'z']

все строки в wordList уникальны

гарантие на то, что секретное слово находится в wordList

количество обращений к Master.guess() <= 10

1 <= wordList.length <= 100

Претесты:
Тест 1:
Input: wordList = ["acckzz","ccbazz","eiowzz","abcczz"], secretWord = "acckzz"

Output: В данном случае, при вызове метода Master.guess() ,
передав каждое слово из wordList, мы гарантированно
меньше, чем за 11 попыток, найдем наше секретное слово.

Тест 2:
Input: wordList = ["acckzz","ccbazz","eiowzz","abcczz", "abcctt", "abccyy", "abccpz", "abccjz", "abcczn", "abccer", "abcclk"],
secretWord = "abcclk"

Output: В данном тесте уже не получится гарантированно уложиться в
10 вызовов методаMaster.guess(),если действовать так же,
как и для предыдущего теста.
"""
from random import choice


def gue(word, words):
    if word in words:
        secret_word = list("acckzz")
        word = list(word)
        count = 0
        for i in range(6):
            if word[i] == secret_word[i]:
                count += 1
        return count
    return -1


def guess(words, word):
    letters_Matched = 0
    for i in range(6):
        if words[i] == word[i]:
            letters_Matched += 1
    return letters_Matched


guessed_or_not = False
WordList = ["acckzz","ccbazz","eiowzz","abcczz"]
count = 0
letterGuessed = 0
while count < 10 and letterGuessed != 6:
    word = choice(WordList)
    letterGuessed = gue(word, WordList)
    candidates = []
    for words in WordList:
        if letterGuessed == guess(words, word):
            candidates.append(words)
    WordList = candidates
else:
    guessed_or_not = True
if guessed_or_not:
    print('YES')
else:
    print('NO')
