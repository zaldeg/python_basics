import time


class TrafficLight:
    __color = (
        ("red", 7, "STOP!", "\033[31m"),
        ("amber", 2, "GET READY!", "\033[33m"),
        ("green", 7, "GO!", "\033[32m"),
        ("amber", 2, "GET READY!", "\033[33m"),
    )

    def running(self, times):
        self.times = times
        for t in range(self.times):
            for i in self._TrafficLight__color:
                print(f"{i[3]}{i[2]}")
                time.sleep(i[1])


TIMES = 1

a = TrafficLight()
a.running(TIMES)
