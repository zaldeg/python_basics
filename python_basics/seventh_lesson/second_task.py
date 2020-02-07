from abc import ABC, abstractmethod


class Clothers:
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_consumption(self):
        pass


class Suit(Clothers):
    @property
    def fabric_consumption(self):
        return 2 * self.param + 0.3


class Coat(Clothers):
    @property
    def fabric_consumption(self):
        return self.param / 6.5 + 0.5


s = Suit(1)
c = Coat(1)
print(s.fabric_consumption)
print(c.fabric_consumption)

