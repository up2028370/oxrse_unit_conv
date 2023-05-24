from si import *
from meta.classes import Unit

# second
minute = Unit(name='minute', abbr='min', si=second, to_si_fun=lambda n: n * 60)
# min shadows the builtin function 'min'

hour = Unit(name='hour', abbr='h', si=second, to_si_fun=lambda n: n * 3600)
h = hour

# meter
kilometer = Unit(name='kilometer', abbr="km", si=meter, to_si_fun=lambda n: n * 1000)
km = kilometer

mile = Unit(name='mile', abbr='mile', si=meter, to_si_fun=lambda n: n * 1_609.344)

milimeter = Unit(name='milimeters', abbr='mm', si=meter, to_si_fun=lambda n: n / 1000)

# meter_sq


# meter_cu

# kilogram

# stone

stone = Unit(name='stone', abbr='st', si=kilogram, to_si_fun=lambda n: n * 0.157473)
st = stone

pound = Unit(name='pound', abbr='lb', si=kilogram, to_si_fun=lambda n: n * 0.4535924)
lb = pound

# ampere

# kelvin

# mole

# candela
sparkle = Unit(name='sparkle', abbr='sp', si=candela, to_si_fun=lambda n: n * 5)
