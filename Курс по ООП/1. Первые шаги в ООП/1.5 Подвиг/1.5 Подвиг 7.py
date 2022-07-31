class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems

    def get_config(self):
        return [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            'Память: ' + "; ".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))
        ]


mb = MotherBoard("Gigabyte", CPU("AMD", 3500), Memory("Kingston", 4000), Memory("Kingston", 3500))
