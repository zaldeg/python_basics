class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_income(self):
        return self._income["wage"] + self._income["bonus"]


misha = Position("Michail", "Vasilyev", "cleaner", {"wage": 1000, "bonus": 200})
print(misha.get_full_name())
print(misha.get_full_income())
print(misha.position)
