class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Rendering started!")


class Pen(Stationery):
    def draw(self):
        print("Writing with a pen")


class Pencil(Stationery):
    def draw(self):
        print("Painting with a pencil have started!")


class Handle(Stationery):
    def draw(self):
        print("We have started write on flipchart")


p = Pen("aaaa")
pl = Pencil("bbbbb")
h = Handle("ccccc")

p.draw()
pl.draw()
h.draw()
print(p.title)
print(pl.title)
print(h.title)
