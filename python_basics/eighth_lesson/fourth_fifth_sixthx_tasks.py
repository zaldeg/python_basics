class Wearhouse:
    wearhouse_data = []
    info = {"Copier": 0, "Printer": 0, "Scanner": 0}

    def __init__(self, wearhouse_name):
        self.wearhouse_name = wearhouse_name

    def reception(self, equipment, number):
        self.equipment = equipment
        self.number = number
        try:
            _ = 7 / self.number
            Wearhouse.wearhouse_data.append(self.equipment.info)
            Wearhouse.info[self.equipment.info[2]] += self.number
        except TypeError:
            print("Enter number not over type")

    def issuance(self, placement, equipment, number):
        self.placement = placement
        self.equipment = equipment
        self.number = number
        try:
            _ = 7 / self.number
            if Wearhouse.info[self.equipment.info[2]] >= self.number:
                Wearhouse.info[self.equipment.info[2]] -= self.number
                print(
                    f"You take from {self.wearhouse_name} {self.number} {self.equipment.info[2]} to {self.placement}"
                )
            else:
                print("You want to take to much stuff")
        except TypeError:
            print("Enter number not over type")


class OfficeEquipment:
    def __init__(self, brand, weight):
        self.brand = brand
        self.weight = weight


class Printer(OfficeEquipment):
    def __init__(self, brand, weight, oe_type, speed):
        super().__init__(brand, weight)
        self.info = [brand, weight, oe_type, speed]


class Scanner(OfficeEquipment):
    def __init__(self, brand, weight, oe_type, dpi):
        super().__init__(brand, weight)
        self.info = [brand, weight, oe_type, dpi]


class Copier(OfficeEquipment):
    def __init__(self, brand, weight, oe_type, something):
        super().__init__(brand, weight)
        self.info = [brand, weight, oe_type, something]


some_wearhouse = Wearhouse("Geekbrains")
print(some_wearhouse.wearhouse_name)
p = Printer("Hp", 3, "Printer", "20 per min")
s = Scanner("Epson", 5, "Scanner", "300 dpi")
c = Copier("Xerox", 8, "Copier", "RED")
some_wearhouse.reception(p, 3)
some_wearhouse.reception(s, "b")
some_wearhouse.reception(c, 3)
print(some_wearhouse.wearhouse_data)
print(some_wearhouse.info)
some_wearhouse.issuance("toilet", p, "b")
print(some_wearhouse.info)
