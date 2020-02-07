class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            print("Number of cells can't be less then one!!!")

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    # def __truediv__(self, other):
    #     """ var with round """
    #     if self.number_of_cells > other.number_of_cells:
    #         return Cell(round(self.number_of_cells / other.number_of_cells))
    #     else:
    #         print("Number of cells can't be less then one!!!")

    def __truediv__(self, other):
        """ var with integer devision """
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells // other.number_of_cells)
        else:
            print("Number of cells can't be less then one!!!")

    def __str__(self):
        return str(self.number_of_cells)

    def make_order(self, order):
        self.order = order
        self.string = ""
        self.tmp = self.number_of_cells
        while self.tmp - self.order > 0:
            self.string += "*" * self.order + "\n"
            self.tmp -= self.order
        self.string += "*" * self.tmp
        return self.string


first_cells = Cell(11)
second_cells = Cell(6)
print(first_cells + second_cells)
print(first_cells - second_cells)
print(first_cells * second_cells)
print(first_cells / second_cells)
a = first_cells * second_cells
print(a.make_order(7))
