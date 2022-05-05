# TODO.01 Получить у юзера список купленных продуктов и вывести их на экран обратно в алфавитном порядке
# переменная содержащая список продуктов нашего пользователя
# user = ["coca-cola", "fruit", "aqua", 'chandler', 'Karl', 'ice', 'ice-cream', 'iphone', 'home']
# user.sort() #отсортировали нащ список
# user.reverse() # мы его перевернули
# print(user)
# TODO.02 Получить у юзера список купленных продуктов и их стоимость, отсортировать их по цене, самые дорогие выше, и выдать сумму потраченную
karl = {
    "coca-cola": 120,
    "fruit": 230,
    "aqua": 1,
    'chandler': 100000,
    'Karl': 4,
    'ice': 70,
    'ice-cream': 12,
    'iphone': 1200,
    'home': 7000
}
#я прописала словарь чтобы привезать сумму к определенному товару
sum_product = sum(karl.values()) #суммировали все потраценные деньги на товар
name_b= karl.keys()

name = list(name_b)
name.sort()
name.reverse()
print(name)
# #
# def sorter():
#     for products, summ in karl.items():
#         print(f'{karl}lol')
#         if summ[products] >= sum(summ) / len(summ):
#             if karl.values() >= summ.numerator:
#                 print(karl)
#     for i in karl.keys():
#         k = list(i)
#         k = tuple(k)
#         v = list(karl.values())
#         v = tuple(v.sort())
#         h = {k: v}
#         karl.update([h])
# key = list(karl.keys())
# value_ = list(karl.values())
# # item = karl.items()
# print(f'{key}:{value_}')
# def u():
#     for i in karl.keys():
#         g = list(karl.values())
#         g.sort()
#         g.reverse()
#         # n = karl.values(g)
#
#         print(karl.fromkeys(i[g]))
#     # if i.numerator >= karl.keys()
print(f'список всех покупок-{karl}\n сумма потраченных денег-{sum_product}')
# TODO.03 Получить у юзера ссылку на вебсайт и открыть ее браузере
# import re
import webbrowser
#здесь происходит запрос на ссылку
user_1 = input('введите ссылку на сайт (она обязанна содержать начало https://)')
webbrowser.open(user_1, new=0, autoraise=True)
# https://docs-python.ru/standart-library/modul-re-python/

# class ValidLink:
#     def is_valid(self):
#         link = re.match(r'^(https|http)\w//[A-z0-9].(ru|com|kg)/\D\d', user_1)
#         print()link
# g = ValidLink()
# print(g.is_valid())
# TODO.09 Расскажи какие уровни нормализации надо учитывать при создании баз данных
# нужно учитывать создание самой таблицы , сразу расмотреть какие нужны поля , сколько памяти потребуется