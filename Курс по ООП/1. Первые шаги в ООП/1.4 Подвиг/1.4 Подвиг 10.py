class Translator:
    dict = dict()

    def add(self, eng, rus):
        if eng in Translator.dict:
            Translator.dict[eng] += (rus, )
        else:
            Translator.dict[eng] = (rus, )
        return Translator.dict

    def remove(self, eng):
        del Translator.dict[eng]

    def translate(self, eng):
        return list(Translator.dict[eng])


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))
