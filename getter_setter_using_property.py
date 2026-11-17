class Celsius:
    def __init__(self, name, value):
        self.name = name
        self._temp = value

    @property
    def temperature(self):
        return self._temp

    @temperature.setter
    def temperature(self, value):
        if value < 100:
            raise ValueError(f"Almost there, {100 - value} left")
        self._temp = value


celsious_n = Celsius("Boiling point of water", 100)
print(celsious_n.temperature)
celsious_n.temperature = 500
print(celsious_n.temperature)
