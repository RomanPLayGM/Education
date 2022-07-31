# from this import s


# class Backstage:
#     left_count_mic = 0
#     right_count_mic = 0

#     _order_in = {}
#     _order_out = {}

#     def __init__(self, start, end, in_, out_):
#         self.start = start
#         self.end = end
#         self.in_ = in_
#         self.out_ = out_
#         # self._update_order(self.start, self.end, self.out_, "in_")
#         # self._update_order(self.end, self.start, self.in_, "out_")
#         self._update_order_in(self.start, self.end, self.out_)
#         self._update_order_out(self.start, self.end, self.in_)

#     @classmethod
#     def _update_order_in(cls, start_time, end_time, out_):
#         if cls._order_in.get(start_time):
#             cls._order_in[start_time].add((end_time, out_))
#         else:
#             cls._order_in[start_time] = {(end_time, out_)}

#     @classmethod
#     def _update_order_out(cls, start_time, end_time, out_):
#         if cls._order_out.get(start_time):
#             cls._order_out[start_time].add(tuple(end_time, out_))
#         else:
#             cls._order_out[start_time] = {(end_time, out_)}
# Как можно было сделать
# @classmethod
# def _update_order(cls, start_: int, end_: int, in_or_out_, name: str):
#     """
#     order_in = {
#         0: {100},
#         50: {150, 250},
#         120: {200}
#     }
#     order_out = {
#         100: {0},
#         150: {50},
#         200: {120},
#         250: {50}
#     }
#     """
#     attrs = {
#         'in_': (cls._order_in, in_or_out_),
#         'out_': (cls._order_out, in_or_out_)
#     }
#
#     # keys = {
#     #     "in_": start_time, end_time
#     #     "out_": end_time, start_time
#     # }
#
#     if attrs[name][0].get(start_):
#         attrs[name][0][start_].add((end_, attrs[name][1]))
#     else:
#         attrs[name][0][start_] = {(end_, attrs[name][1])}
#     """
#     if cls.order_in.get(start_time):
#         cls.order_in[name][start_].add(end_)
#     else:
#         attrs[name][start_] = {end_}
#     """

#     @classmethod
#     def _update_count_mic(cls):
#         ...

#     def _method(self):
#         ...


# a = Backstage(0, 100, "l", "r")
# b = Backstage(50, 250, "r", "r")
# c = Backstage(120, 200, "r", "l")
# print(a._order_in)
# print(a._order_out)
# Backstage(50, 150, l, l)
# Backstage(120, 200, r, l)
# Backstage(50, 250, r, r)
# res = (Backstage(0, 100, l, r), Backstage(50, 150, l, l), Backstage(100, 200, r, l), Backstage(50, 250, l, l))
# sum(res) -> Backstage.left_count_mic = 2, Backstage.right_count_mic = 1


class Backstage:
    """
    Пример:
        Backstage(0, 100, 'l', 'r')
        Backstage(50, 150, 'l', 'l')
        Backstage(120, 200, 'r', 'l')
        Backstage(50, 250, 'r,' 'r')
    """
    left_count_mic = 0
    right_count_mic = 0

    _order_in = {}
    _order_out = {}

    chains = []
    cash_suitable_items = set()
    help_cash = set()

    def __init__(self, start_time, end_time, in_, out_):
        self.start_time = start_time
        self.end_time = end_time
        self.in_ = in_
        self.out_ = out_

        self._update_order_in(self, self.start_time)
        self._update_order_out(self, self.end_time)

    @classmethod
    def _update_order_in(cls, instance, start_time: int):
        """
        :param instance: ...
        :param start_time: Время выхода на сцену

        >>> _order_in = {
        >>>     0: {Backstage(0, 100, 'l', 'r')},
        >>>     50: {Backstage(50, 150, 'l,' 'l'), Backstage(50, 250, 'r,' 'r')},
        >>>     120: {Backstage(120, 200, 'r', 'l')}
        >>> }
        """
        if cls._order_in.get(start_time):
            cls._order_in[start_time].append(instance)
        else:
            cls._order_in[start_time] = [instance]

    @classmethod
    def _update_order_out(cls, instance, end_time: int):
        """
        :param instance: ...
        :param end_time: Время ухода со сцены

        >>> _order_out = {
        >>>     100: {Backstage(0, 100, 'l', 'r')},
        >>>     150: {Backstage(50, 150, 'l', 'l')},
        >>>     200: {Backstage(120, 200, 'r', 'l')},
        >>>     250: {Backstage(50, 250, 'r,' 'r')}
        >>> }
        """
        if cls._order_out.get(end_time):
            cls._order_out[end_time].add(instance)
        else:
            cls._order_out[end_time] = {instance}

    # Возможно не staticmethod

    def _calculate_distance(self, order_in: dict, end_time: int) -> 'Backstage':
        """
        Description

        :param order_in: ...
        :param end_time: ...

        :return:
        """
        order_keys = list(order_in)
        distance = None
        instance = None
        for i in order_keys:
            new_distance = end_time - i
            if 0 >= new_distance:
                if distance is None or abs(new_distance) < abs(distance):
                    distance = new_distance
                    elements = order_in[i]
                    if len(elements) > 1:
                        # new_elements = []
                        min_end_time = -1
                        min_elements = None
                        for j in range(len(elements)):
                            if self.out_ == elements[j].in_:
                                # new_elements.append(elements[j])
                                if min_end_time == -1 or elements[j].end_time < min_end_time:
                                    min_end_time = elements[j].end_time
                                    min_elements = elements[j]
                                # if elements[j].end_time < min_end_time:
                                #     min_end_time = elements[j].end_time
                                #     min_elements = elements[j]
                        instance = min_elements
                        # Backstage.cash_suitable_items.add(instance), Backstage.cash_suitable_items.add(self)
                        if instance is not None:
                            Backstage.help_cash.add(self)
                        # if len(new_elements) == 0:
                        #     instance = None
                        # else:
                        #     instance = min(new_elements, key=lambda x: x.end_time)
                    else:
                        if len(elements) > 0:
                            if self.out_ == elements[0].in_:
                                instance = order_in[i][0]
                                # Backstage.cash_suitable_items.add(instance), Backstage.cash_suitable_items.add(
                                #     self)
                        if instance is not None:
                            Backstage.help_cash.add(self)
        print(self, instance)
        return instance

    # Метод для отладки
    def run(self):
        return self._calculate_distance(self._order_in, self.end_time)

    # Пример написания/документирования метода
    @classmethod
    def _update_order(cls, start_time: int, end_time: int, in_: str, out_: str, name: str):
        """
        :param start_time: Время выхода на сцену
        :param end_time: Время ухода со сцены
        :param in_: Сторона выхода на сцену (l или r)
        :param out_: Сторона ухода со сцены (l или r)
        :param name: Время выхода на сцену

        :return None:

        >>> _order_in = {
        >>>     0: {(100, 'r')},
        >>>     50: {(150, 'l'), (250, 'r')},
        >>>     120: {(200, 'l')}
        >>> }
        >>> _order_out = {
        >>>     100: {(0, 'l')},
        >>>     150: {(50, 'l')},
        >>>     200: {(120, 'r')},
        >>>     250: {(50, 'r')}
        >>> }
        """
        attr_keys = {
            'in_': cls._order_in,
            'out_': cls._order_out
        }
        time_keys = {
            'in_': (start_time, end_time),
            'out_': (end_time, start_time)
        }
        place_keys = {
            'in_': in_,
            'out_': out_
        }
        '''
        if cls._order_in.get(start_time):
            cls._order_in[start_time].add((end_time, out_))
        else:
            cls._order_in[start_time] = {(end_time, out_)}

        или 

        if cls._order_out.get(end_time):
            cls._order_out[end_time].add((start_time, in_))
        else:
            cls._order_out[end_time] = {(start_time, in_)}
        '''
        if attr_keys[name].get(time_keys[name][0]):
            attr_keys[name][time_keys[name][0]].add((time_keys[name][1], place_keys[name]))
        else:
            attr_keys[name][time_keys[name][0]] = {(time_keys[name][1], place_keys[name])}

    @classmethod
    def check_None(cls, element, cash):
        # print(element[0], element[0].run())
        if element[0].run() is None:
            for j in cash:
                if j == element[0]:
                    return True
            # cls.chains.append(element)
            return True

    @classmethod
    def help_check_chains(cls, k, i, left_or_right, chain, max_i):
        for j in range(k, i):
            if left_or_right.start_time > cls.chains[chain][max_i].start_time:
                cls.chains[chain].append(left_or_right)
                break
            else:
                if left_or_right.start_time <= cls.chains[chain][j].start_time:
                    if left_or_right.start_time < cls.chains[chain][j].start_time:
                        cls.chains[chain] = cls.chains[chain][:j] + [left_or_right] + cls.chains[chain][j:]
                        break
                    else:
                        break

    @classmethod
    def check_chains(cls, left_or_right_1, left_or_right_2, left_or_right_3):
        for chains in range(len(cls.chains)):
            print(cls.chains[chains], 25352378999)
            for i in range(len(cls.chains[chains])):
                if left_or_right_1 == cls.chains[chains][i]:
                    if left_or_right_3 == "left":
                        cls.help_check_chains(i, len(cls.chains[chains]), left_or_right_2, chains, -1)
                    else:
                        cls.help_check_chains(0, i, left_or_right_2, chains, i)
                    break
        return True

    @classmethod
    def check(cls, elements):
        if len(cls.chains) == 0:
            cls.chains.append([elements[0], elements[0].run()])
            cls.cash_suitable_items.add(elements[0]), cls.cash_suitable_items.add(elements[0].run())
        else:
            left_element = elements[0]
            print(left_element, 121212121)
            right_element = left_element.run()
            print(right_element, 121234425)
            print(cls.cash_suitable_items)
            print(cls.help_cash)
            for j in range(len(cls.cash_suitable_items)):
                if len(cls.cash_suitable_items) > 0:
                    if list(cls.cash_suitable_items)[j] == left_element:
                        print(232778565)
                        if cls.check_chains(left_element, right_element, "left"):
                            break
                    elif list(cls.cash_suitable_items)[j] == right_element:
                        print(2414153)
                        if cls.check_chains(right_element, left_element, "right"):
                            break
                    else:
                        cls.cash_suitable_items.add(left_element), cls.cash_suitable_items.add(right_element)
            else:
                print(99999999)
                cls.chains.append([left_element, right_element])
                cls.cash_suitable_items.add(left_element), cls.cash_suitable_items.add(right_element)

    @classmethod
    def out(cls):
        for i in cls._order_in:
            elements = cls._order_in[i]
            if len(elements) > 1:
                for element in elements:
                    if cls.check_None([element], cls.cash_suitable_items):
                        continue
                    cls.check([element])
            else:
                if cls.check_None(elements, cls.cash_suitable_items):
                    continue
                cls.check(elements)
        print(cls._order_in)
        print(cls.chains)
        print(cls.cash_suitable_items)
        print(cls.help_cash)


# res = (Backstage(0, 100, l, r), Backstage(50, 150, l, l), Backstage(100, 200, r, l), Backstage(50, 250, l, l))
# sum(res) -> Backstage.left_count_mic = 2, Backstage.right_count_mic = 1

# input(): 0 100 l r -> input().split(): ['0', '100', 'l', 'r']
Backstage(230, 270, 'l', 'l')
x = Backstage(0, 100, 'l', 'r')
Backstage(50, 150, 'l', 'l')
# Backstage(100, 200, 'r', 'l')
Backstage(50, 250, 'r', 'r')
Backstage(100, 200, 'r', 'l')
x.out()
#print(x._order_in)
# print(x.run().end_time)
# print(x._order_in)
# x.out()
y = []
for i in range(len(y)):
    print(y[i])
    if i == 6:
        break
else:
    print(999999)

t1 = 3
t = [1, 2, 4]
for i in range(len(t)):
    if t1 > t[-1]:
        t.append(t1)
        print(t, 0)
        break
    else:
        if t1 <= t[i]:
            if t1 < t[i]:
                t = t[:i] + [t1] + t[i:]
                print(t, 2)
                break
            else:
                print(t, 3)
                break
else:
    print(1)


