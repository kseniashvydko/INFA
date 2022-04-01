import csv


class Bolt_detail:
    def __init__(self, height, width, length, weight, color=None):
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight
        self.color = color
    def Height(self):
        print(f"высота детали{self.height}")
    def Length(self):
        print(f"длина детали{self.length}")
    def Width(self):
        print(f"ширина детали{self.width}")
    def Mass(self):
        print(f"масса детали{self.mass}")




class Color_ceh_queue:
    def __init__(self):
        self.items = [] #детали все
    def isEmpty(self): #наличие элементов в очередери
        return self.items == []

    def file(self):
        with open("детали", mode="w", encoding='utf-8') as file:
            file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
            for i in range(0, self.size - 1):
                file_writer(f'в цеху {self.size} деталей')
                file_writer(
                    f'Деталь 1: {self.queue[i].height},{self.queue[i].width},{self.queue[i].lenght},{self.queue[i].weight}'
                    f'{self.queue[i].color}')





Detail = Bolt_detail(12, 13, 3,4)
Detail.Height()
Detail.Length()
Detail.Width()
Detail.Mass()

