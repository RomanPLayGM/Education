TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        object = None
        if TYPE_OS == 1:
            object = super().__new__(DialogWindows)
        else:
            object = super().__new__(DialogLinux)
        object.name = args[0]
        return object
# здесь объявляйте класс Dialog
