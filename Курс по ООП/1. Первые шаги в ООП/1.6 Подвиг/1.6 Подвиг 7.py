class SingletonFive:
    instance = None
    count = 0

    def __new__(cls, *args, **kwargs):
        if cls.count < 5:
            cls.instance = super().__new__(cls)
            cls.count += 1

        return cls.instance

    def __init__(self, name):
        self.name = name


