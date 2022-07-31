class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def closed(self):
        print("Отображение данных закрыто")

    def show(self):
        return " ".join(map(str, self.data))

    def show_table(self):
        if self.is_show:
            self.show()
        else:
            self.closed()

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {self.show()}")
        else:
            self.closed()

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {self.show()}")
        else:
            self.closed()

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
