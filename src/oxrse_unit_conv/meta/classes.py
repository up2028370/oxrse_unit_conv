# Class definition
from copy import deepcopy
from typing import Callable, Union, List

Number = Union[float, int]


class DimensionError(TypeError):
    pass


class ExponentError(TypeError):
    pass


class BaseUnit:
    dimension: str
    exponent: int

    def __init__(self, name: str = "", abbr: str = "", exponent: int = 1):
        self.name = name
        self.dimension = abbr
        self.exponent = exponent

    def matches(self, target: 'BaseUnit') -> bool:
        if target.dimension != self.dimension:
            return False
        return target.exponent == self.exponent


class SIUnit(BaseUnit):

    def __init__(self, name: str = "", abbr: str = "", exponent: int = 1):
        super().__init__(name=name, abbr=abbr, exponent=exponent)
        self.si_units = []

    def to_si(self, x: Number) -> float:
        return float(x)

    def from_si(self, x: Number) -> float:
        return float(x)

    def to_unit(self, number: Number, target_unit: Union['Unit', 'SIUnit']) -> float:
        if self.matches(target_unit):
            return number

        if not self.matches(target_unit.si_unit):
            if self.dimension != target_unit.si_unit.dimension:
                raise DimensionError((
                    f"Cannot convert {self.dimension} to "
                    f"{target_unit.dimension} [{target_unit.si_unit.dimension}]"
                ))
            raise ExponentError((
                f"Cannot convert {self.dimension}^{self.exponent} to "
                f"{target_unit.si_unit.dimension}^{target_unit.si_unit.exponent}"
            ))

        return target_unit.from_si(number)


class Unit(BaseUnit):
    """
    A Unit has a name and SI Unit/s that determine how it converts to other units.
    """
    si_unit: SIUnit
    to_si_fun: Callable[[Number], float]
    from_si_fun: Callable[[Number], float]

    def __init__(
            self,
            name: str,
            abbr: str,
            si: SIUnit,
            to_si_fun: Callable[[Number], float],
            from_si_fun: Callable[[Number], float] = None,
            exponent: Number = 1
    ):
        super().__init__(name=name, abbr=abbr, exponent=exponent)
        self.si_unit = si
        self.to_si_fun = to_si_fun
        if not from_si_fun:
            self.from_si_fun = lambda x: x / self.to_si_fun(1)
        else:
            self.from_si_fun = from_si_fun

    def exponented_conversion(self, number: Number, fun: Callable[[Number], float]) -> float:
        e = self.exponent
        if not isinstance(self.exponent, int):
            raise ExponentError(f"Cannot convert {self.dimension} with non-integer exponent {self.exponent}")
        as_si = number
        while e > 0:
            as_si = fun(as_si)
            e -= 1
        if e < 0:
            while e < 0:
                as_si = fun(as_si)
                e += 1
            as_si = 1 / as_si

        return as_si

    def to_si(self, number: Number) -> float:
        return self.exponented_conversion(number, self.to_si_fun)

    def from_si(self, number: Number) -> float:
        return self.exponented_conversion(number, self.from_si_fun)

    def to_unit(self, number: Number, target_unit: Union['Unit', SIUnit]) -> float:
        as_si = self.to_si(number)

        if self.si_unit.matches(target_unit):
            return as_si

        if not self.si_unit.matches(target_unit.si_unit):
            if self.si_unit.dimension != target_unit.si_unit.dimension:
                raise DimensionError((
                    f"Cannot convert {self.dimension} [{self.si_unit.dimension}] to "
                    f"{target_unit.dimension} [{target_unit.si_unit.dimension}]"
                ))
            raise ExponentError((
                f"Cannot convert {self.si_unit.dimension}^{self.si_unit.exponent} to "
                f"{target_unit.si_unit.dimension}^{target_unit.si_unit.exponent}"
            ))

        return target_unit.from_si(as_si)


def simplify_dimensions(units: List[Union[Unit, SIUnit]]) -> List[Union[Unit, SIUnit]]:
    units_by_abbr = {}
    for u in units:
        if u.dimension not in units_by_abbr.keys():
            units_by_abbr[u.dimension] = deepcopy(u)
        else:
            units_by_abbr[u.dimension].exponent += u.exponent

    return [v for v in units_by_abbr.values()]


def unit_str(units: Union[List[Union[Unit, SIUnit]], Union[Unit, SIUnit]]) -> str:
    if not isinstance(units, list):
        units = [units]
    return ' '.join([f"{u.dimension}{u.exponent if u.exponent != 1 else ''}" for u in units])
