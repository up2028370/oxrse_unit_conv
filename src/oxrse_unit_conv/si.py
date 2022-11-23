# SI Units

# The SI Units form the basis for conversion.
# To convert between units the SI unit is used as a stepping stone -
# the first unit is converted to the SI unit,
# and then the SI unit is converted to the second unit.

from meta import classes

second = classes.SIUnit("second", "s")
s = second

meter = classes.SIUnit("meter", "m")
m = meter
meter_sq = classes.SIUnit("meter_sq", "m", 2)
m2 = meter_sq
meter_cu = classes.SIUnit("meter_cu", "m", 3)
m3 = meter_cu

kilogram = classes.SIUnit("kilogram", "kg")
kg = kilogram

ampere = classes.SIUnit("ampere", "A")
A = ampere

kelvin = classes.SIUnit("kelvin", "K")
K = kelvin

mole = classes.SIUnit("mole", "mol")
mol = mole

candela = classes.SIUnit("candela", "cd")
cd = candela
