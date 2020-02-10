class Matrix:
    def __init__(self, mtrx):
        self.matrix = mtrx

    def __str__(self):
        self.string = ""
        for i in self.matrix:
            for j in i:
                self.string += " " * (6 - len(str(j))) + str(j)
            self.string += "\n\n"
        return self.string

    def __add__(self, other):
        self.tmp = [[0 for i in j] for j in self.matrix]
        for i in range(len(self.tmp)):
            for j in range(len(self.tmp[0])):
                self.tmp[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.tmp)


data = [[1, 36, 3], [-45, 3, 2], [4, 5, 1]]
data_1 = [[2, 1, 3], [5, 2, 1], [2, 3, 4]]
m = Matrix(data)
m_1 = Matrix(data_1)
print(m)
print(m + m_1)
