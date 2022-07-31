# import random
# bank = 0
# cube = 0  # random.random() Кто первый начнет
# print(cube)
# if cube:
#     while True:
#         print(bank, "Сколько всего")
#         bank += int(input())
#         print(bank, "Банк после моего хода")
#         if 79 <= bank <= 88:
#             bank = 89
#         else:
#             if 69 <= bank <= 77:
#                 bank = 78
#             else:
#                 bank += 10
#             print(bank, "Банк после хода бота")
#         if bank >= 100:
#             break
# else:
#     while True:
#         print(bank, "Сколько всего")
#         if bank == 0:
#             bank = 1
#         elif 2 <= bank <= 11:
#             bank = 12
#         elif 13 <= bank <= 22:
#             bank = 23
#         elif 24 <= bank <= 33:
#             bank = 34
#         elif 35 <= bank <= 44:
#             bank = 45
#         elif 46 <= bank <= 55:
#             bank = 56
#         elif 57 <= bank <= 66:
#             bank = 67
#         elif 68 <= bank <= 77:
#             bank = 78
#         elif 79 <= bank <= 88:
#             bank = 89
#         elif 90 <= bank <= 99:
#             bank = 100
#             print(bank, "Банк после робота хода")
#             print("Победа")
#             break
#         print(bank, "Банк после хода робота")
#         bank += int(input())
#         print(bank, "Банк после моего хода")

print("--------------------------------")

bank = 0
i = 0
while True:
    print(bank, "Сколько всего")
    if 90 <= bank <= 99:
        bank = 100
        print(bank, "Банк после робота хода")
        print("Победа")
        break
    bank = int(f"{i}{i + 1}")
    i += 1
    print(bank, "Банк после хода робота")
    bank += int(input())
    print(bank, "Банк после моего хода")
