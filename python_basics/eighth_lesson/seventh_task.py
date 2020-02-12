class Complex_number:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        return Complex_number(
            self.real_part + other.real_part, self.imaginary_part + other.imaginary_part
        )

    def __mul__(self, other):
        return Complex_number(
            self.real_part * other.real_part
            - self.imaginary_part * other.imaginary_part,
            self.real_part * other.imaginary_part
            + self.imaginary_part * other.real_part,
        )

    def __str__(self):
        if self.imaginary_part < 0:
            return f"{self.real_part} - {self.imaginary_part}i"
        else:
            return f"{self.real_part} + {self.imaginary_part}i"


a = Complex_number(2, 1)
b = Complex_number(5, 3)
c = a + b
print(a * b)
print(c)
