import sys


class ListObject:
    def __init__(self, data) -> None:
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = [
#     "Первые шаги в ООП",
#     "Как правильно проходить этот курс",
#     "Концепция ООП простыми словами",
#     "Классы и объекты. Атрибуты классов и объектов"
# ]
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         if not self.next_obj:
#             self.next_obj = obj
#             return
#         else:
#             self.next_obj.link(obj)
#
#
# # считывание списка из входного потока (эту строку не менять)
# lst_in = [
#     "Первые шаги в ООП",
#     "Как правильно проходить этот курс",
#     "Концепция ООП простыми словами"
#     "Классы и объекты. Атрибуты классов и объектов"
# ]
#
# # здесь создаются объекты классов и вызываются нужные методы
# head_obj = ListObject(lst_in[0])
# for data_ in lst_in[1:]:
#     head_obj.link(ListObject(data_))
