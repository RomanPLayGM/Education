class Backstage:
    """
    Зал Большого театра столь велик, что артистам при выступлении необходимо иметь радиомикрофоны.

    В начале и конце спектакля все артисты находятся за кулисами. Артисты выходят на сцену и покидают сцену через
    правую или левую кулису, при этом артист берет с собой один микрофон. Уйдя со сцены, артист оставляет микрофон за
    той кулисой, через которую он ушел.

    Имеется режиссерский план, в котором для каждого артиста указано его прихода и ухода со сцены, а также то,
    через какие кулисы он входит и выходит.

    Определите, какое наименьшее число микрофонов необходимо приготовить режиссеру за каждой кулисой до начала спектакля.

    Формат входных данных Первая строка входный данных содержит натуральное число n, 1<=n<10000. Далее идет n строк –
    инструкции для артистов. Каждая строка состоит из двух чисел и двух букв. Первое число – время выхода артиста от
    начала спектакля в секундах, второе число – время ухода артиста со сцены. Потом идет одна из двух букв "l" или
    "r" в зависимости от того, через какую кулису (левую или правую) приходит артист и еще одна буква, указывающая
    через какую кулису уходит артист. Например, строка "300 500 l r" означает, что актер выходит на сцену в момент
    времении 300 через левую кулису и уходит со сцены в момент 500 через правую кулису.

    Времена приходов и уходов – целые неотрицательные числа, не превосходящие 10000. Строки во входном файле могут
    идти в произвольном порядке, не обязательно упорядоченные по времени. Если в один и тот же момент один артист
    уходит за кулису, а другой выходит из-за этой же кулисы, то он может передать ему микрофон в этот момент.

    Формат выходных данных Программа должна вывести два числа: минимальное количество микрофонов, которое должно быть
    в начале спектакля за левой и за правой кулисами.
    """
    left_count_mic = 0
    right_count_mic = 0

    _order_in = {}
    _order_out = {}

    chains = []
    cash_suitable_items = set()
    help_cash = set()
    del_help_cash = set()
    check_del_cash = 0

    def __init__(self, start_time, end_time, in_, out_):
        self.start_time = start_time
        self.end_time = end_time
        self.in_ = in_
        self.out_ = out_

        self._update_order_in(self, self.start_time)
        self._update_order_out(self, self.end_time)

    @classmethod
    def _update_order_in(cls, instance, start_time: int):
        if cls._order_in.get(start_time):
            cls._order_in[start_time].append(instance)
        else:
            cls._order_in[start_time] = [instance]

    @classmethod
    def _update_order_out(cls, instance, end_time: int):
        if cls._order_out.get(end_time):
            cls._order_out[end_time].add(instance)
        else:
            cls._order_out[end_time] = {instance}

    @classmethod
    def find_a_pair_of(cls, self, elements, instance, i):
        """
        Метод для нахождения пары из нескольких элементов
        :param self:
        :param elements:
        :param instance:
        :return:
        """
        min_end_time = -1
        min_index = 0
        min_elements = None
        K = 0
        for j in range(len(elements)):
            if elements[j] is None:
                continue
            if self.out_ == elements[j].in_:
                if min_end_time == -1 or elements[j].end_time < min_end_time:
                    min_end_time = elements[j].end_time
                    min_elements = elements[j]
                    min_index = j
                    K += 1
        if K > 0:
            instance = min_elements
            cls._order_in[i][min_index] = None
            cls.cash_suitable_items.add(instance), cls.cash_suitable_items.add(self)
        return instance

    @classmethod
    def find_a_pair_from_one(cls, self, elements, instance, i):
        """
        Метод для нахождения пары из одного элемента
        :param self:
        :param elements:
        :param instance:
        :return:
        """
        if self.out_ == elements[0].in_:
            instance = elements[0]
            cls._order_in[i] = [None]
            cls.cash_suitable_items.add(instance), cls.cash_suitable_items.add(self)
        return instance

    @classmethod
    def checking_if_a_pair_is_found_in_the_cache(cls, self, instance):
        """
        Проверка по нахождению пары в кешэ
        :param instance:
        :param self:
        :return:
        """
        cash_help = set()
        for element in cls.cash_suitable_items:
            if element is not None:
                if (self.out_ == element.in_ and self.end_time < element.start_time) or (
                        self.in_ == element.out_ and self.start_time > element.end_time):
                    instance = element
                    cash_help.add(self)
        cls.cash_suitable_items |= cash_help
        return instance

    @classmethod
    def checking_if_the_pair_is_in_the_additional_cache(cls, self, instances):
        """
        Проверка по нахождению пары в доп кешэ
        :param self:
        :param instances:
        :return:
        """
        set_del = set()
        for element in Backstage.help_cash:
            if element is not None:
                instances = element
                if (self.out_ == element.in_ and self.end_time < element.start_time) or (
                        self.in_ == element.out_ and self.start_time > element.end_time):
                    set_del.add(i)
                    cls.cash_suitable_items.add(self), cls.cash_suitable_items.add(element)
        cls.help_cash -= set_del
        return instances

    @classmethod
    def _calculate_distance(cls, self, order_in: dict, end_time: int) -> None:
        """
        Метод ищет потенциальную пару, если находит,
        то добавляет в кэш - пар, а если нет,
        то добавляет в доп кэш - без пар 'Одиночек'
        :param order_in:
        :param end_time:
        :return:
        """
        order_keys = list(order_in)
        distance = None
        instance = None
        for i in order_keys:
            new_distance = end_time - i
            print(new_distance)
            if 0 >= new_distance:
                if distance is None or abs(new_distance) < abs(distance):
                    distance = new_distance
                    elements = order_in[i]
                    if len(elements) > 1:
                        instance = cls.find_a_pair_of(self, elements, instance, i)
                    else:
                        if order_in[i][0] is None:
                            continue
                        if len(elements) > 0:
                            instance = cls.find_a_pair_from_one(self, elements, instance, i)
        if instance is None:
            if len(Backstage.cash_suitable_items) > 0:
                instance = cls.checking_if_a_pair_is_found_in_the_cache(self, instance)
            if len(Backstage.help_cash) > 0:
                instance = cls.checking_if_the_pair_is_in_the_additional_cache(self, instance)
        if instance is None:
            cls.help_cash.add(self)
        print(self, instance)
        return instance

    # Метод для отладки
    def run(self):
        return self._calculate_distance(self, self._order_in, self.end_time)

    @classmethod
    def check_None(cls, element):
        if element is None:
            return True

    @classmethod
    def help_check_chains(cls, start, end, element, chain, max_i):
        for index in range(start, end):
            if (element.start_time <= cls.chains[chain][max_i].end_time) and (
                    element.end_time >= cls.chains[chain][max_i].end_time):
                cls.check_del_cash = 1
                break
            if element.start_time >= cls.chains[chain][max_i].end_time:
                cls.chains[chain].append(element)
                break
            else:
                if element.end_time <= cls.chains[chain][index].start_time:
                    if element.start_time < cls.chains[chain][index].start_time:
                        cls.chains[chain] = cls.chains[chain][:index] + [element] + cls.chains[chain][index:]
                    else:
                        break

    @classmethod
    def check_chains(cls, cash_element, help_cash_element, side):
        for index_chain in range(len(cls.chains)):
            chain = cls.chains[index_chain]
            for element_chain in range(len(chain)):
                if chain[element_chain] == cash_element:
                    if side == "left":
                        cls.help_check_chains(0, element_chain, help_cash_element,
                                              index_chain, element_chain)
                    elif side == "right":
                        cls.help_check_chains(element_chain, len(cls.chains[index_chain]), help_cash_element,
                                              index_chain, -1)
                    break

        return True

    @classmethod
    def check(cls):
        print(cls.cash_suitable_items, 1)
        print(cls.help_cash, 2)
        for cash_index in range(len(cls.cash_suitable_items)):
            cash_element = list(cls.cash_suitable_items)[cash_index]
            for help_cash_index in range(len(cls.help_cash)):
                help_cash_element = list(cls.help_cash)[help_cash_index]
                if cash_element.start_time >= help_cash_element.end_time and cash_element.in_ == help_cash_element.out_:
                    if cls.check_chains(cash_element, help_cash_element, "left"):
                        if cls.check_del_cash == 1:
                            cls.check_del_cash = 0
                            continue
                        cls.del_help_cash.add(help_cash_element)
                        continue
                elif cash_element.end_time <= help_cash_element.start_time and cash_element.out_ == help_cash_element.in_:
                    print(22324242424)
                    if cls.check_chains(cash_element, help_cash_element, "right"):
                        if cls.check_del_cash == 1:
                            cls.check_del_cash = 0
                            continue
                        cls.del_help_cash.add(help_cash_element)
                        continue

    @classmethod
    def del_cash(cls):
        print(cls.del_help_cash, "del help cash")
        print(cls.cash_suitable_items, "cash")
        print(cls.help_cash, "help cash")
        if len(cls.del_help_cash) > 0:
            cls.cash_suitable_items |= cls.del_help_cash
            cls.help_cash -= cls.del_help_cash

    @classmethod
    def out(cls):
        for i in cls._order_in:
            print(cls._order_in)
            elements = cls._order_in[i]
            if len(elements) > 1:
                for element in range(len(elements)):
                    element_1 = elements[element]
                    print(element_1, elements)
                    if element_1 is None:
                        continue
                    check_1 = element_1.run()
                    cls._order_in[i][element] = None
                    if cls.check_None(check_1):
                        continue
                    cls.chains.append([element_1, check_1])
                pass
            else:
                element_1 = elements[0]
                if element_1 is None:
                    continue
                check = element_1.run()
                cls._order_in[i][0] = None
                if cls.check_None(check):
                    continue
                cls.chains.append([element_1, check])
        cls.check()
        cls.del_cash()
        print(cls.chains, 1211)
        print(cls.cash_suitable_items)
        print(cls.help_cash)

    @classmethod
    def answer(cls):
        cls.out()
        for element in cls.chains:
            if element[0].in_ == 'l':
                cls.left_count_mic += 1
            elif element[0].in_ == 'r':
                cls.right_count_mic += 1
        for element in cls.help_cash:
            if element.in_ == 'l':
                cls.left_count_mic += 1
            elif element.in_ == 'r':
                cls.right_count_mic += 1
        return cls.left_count_mic, cls.right_count_mic


n = int(input())
x = None
for i in range(n):
    start, end, in_, out_ = map(str, input().split())
    x = Backstage(int(start), int(end), in_, out_)
x.answer()
print(x.left_count_mic, x.right_count_mic)

# res = (Backstage(0, 100, l, r), Backstage(50, 150, l, l), Backstage(100, 200, r, l), Backstage(50, 250, l, l))
# sum(res) -> Backstage.left_count_mic = 2, Backstage.right_count_mic = 1

# input(): 0 100 l r -> input().split(): ['0', '100', 'l', 'r']
# Backstage(230, 270, 'l', 'l')
# x = Backstage(0, 100, 'l', 'r')
# # Backstage(120, 150, 'l', 'l')
# # Backstage(120, 230, 'l', 'l')
# Backstage(50, 150, 'l', 'l')
# Backstage(50, 250, 'r', 'r')
# Backstage(100, 200, 'r', 'l')
# x.answer()
# Ввод:
# Ввод 1:
# 5
# 230 270 l l
# 0 100 l r
# 50 150 l l
# 50 250 r r
# 100 200 r l
# Ввод 2:
# 3
# 0 100 l r
# 50 150 l l
# 100 200 r l
# Ввод 3:
# 4
# 0 100 l r
# 50 150 l l
# 50 250 r r
# 100 200 r l
# Ввод 4:
# 4
# 884 950 l r
# 855 989 l r
# 351 433 l l
# 525 815 l l
# Ввод 5:
# 7
# 122 137 l l
# 762 924 l l
# 521 746 l l
# 274 527 l r
# 682 942 l l
# 697 886 l l
# 361 628 l l
# def _calculate_distance(self, order_in: dict, end_time: int) -> 'Backstage':
#     order_keys = list(order_in)
#     distance = None
#     instance = None
#     for i in order_keys:
#         if order_in[i][0] is None:
#             continue
#         new_distance = end_time - i
#         if 0 >= new_distance:
#             if distance is None or abs(new_distance) < abs(distance):
#                 distance = new_distance
#                 elements = order_in[i]
#                 if len(elements) > 1:
#                     min_end_time = -1
#                     min_index = 0
#                     min_elements = None
#                     K = 0
#                     for j in range(len(elements)):
#                         if self.out_ == elements[j].in_:
#                             if min_end_time == -1 or elements[j].end_time < min_end_time:
#                                 min_end_time = elements[j].end_time
#                                 min_elements = elements[j]
#                                 min_index = j
#                                 K += 1
#                     if K > 0:
#                         instance = min_elements
#                         Backstage._order_in[i][min_index] = None
#                         Backstage.cash_suitable_items.add(instance), Backstage.cash_suitable_items.add(self)
#                 else:
#                     if len(elements) > 0:
#                         if self.out_ == elements[0].in_:
#                             instance = order_in[i][0]
#                             Backstage._order_in[i] = [None]
#                             Backstage.cash_suitable_items.add(instance), Backstage.cash_suitable_items.add(self)
#     if instance is None:
#         if len(Backstage.cash_suitable_items) > 0:
#             for i in Backstage.cash_suitable_items:
#                 if i is not None:
#                     if (self.out_ == i.in_ and self.end_time < i.start_time) or (
#                             self.in_ == i.out_ and self.start_time > i.end_time):
#                         instance = i
#                         Backstage.cash_suitable_items.add(self)
#         if len(Backstage.help_cash) > 0:
#             set_del = set()
#             for i in Backstage.help_cash:
#                 if i is not None:
#                     if (self.out_ == i.in_ and self.end_time < i.start_time) or (
#                             self.in_ == i.out_ and self.start_time > i.end_time):
#                         instance = i
#                         set_del.add(instance)
#                         Backstage.cash_suitable_items.add(self), Backstage.cash_suitable_items.add(instance)
#             Backstage.help_cash -= set_del
#     if instance is None:
#         Backstage.help_cash.add(self)
#     return instance
