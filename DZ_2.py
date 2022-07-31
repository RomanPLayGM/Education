import re

string = r"""
Привет, Артем! Как твои дела?
Здравстуйте, Олег, что делаете завтра утром?
Окей, Мария, я вас услышала
Имя:Дмитрий
"Санкт-Петербург!" - Елена воскликнула
"""
patter = r"((\:| )[А-Я]{1}[а-я]{1,25}(\!|\,))|((\:)[А-Я]{1}[а-я]{1,25})|(\- [А-Я]{1}[а-я]{1,25})"
match = re.findall(patter, string)
for i in match:
    for j in i:
        if re.fullmatch(patter, j):
            string2 = ""
            for y in j:
                if y != " " and y != "!" and y != "-" and y != "," and y != ":":
                    string2 += y
            print(string2)
