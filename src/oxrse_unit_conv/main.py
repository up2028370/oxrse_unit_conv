# Click interface to allow running from command line
from oxrse_unit_conv import units
from oxrse_unit_conv.meta import classes
import click
import logging


logger = logging.getLogger(__file__)


@click.command()
@click.argument("number", type=float)
@click.argument("unit")
@click.argument("to")
def click_convert(number, unit, to):
    """Convert from one unit to another.

    Units should be specified according to a name exported in units.py (which also exports the units in si.py)

    Usage: N X [Y]
    N: Number of unit X
    X: Unit to convert from
    Y: Unit to convert to (optional, defaults to appropriate SI unit)
    """
    click.echo(convert(number, unit, to))


def convert(number: classes.Number, unit: str, to: str):
    logging.debug(f"Call: {number}: {unit} -> {to}")

    my_unit: units.Unit = getattr(units, unit)
    if not isinstance(my_unit, classes.BaseUnit):
        raise TypeError(f"{unit} does not correspond to a known unit.")
    if to:
        target_unit = getattr(units, to)
        if not isinstance(target_unit, classes.BaseUnit):
            raise TypeError(f"{to} does not correspond to a known unit.")
    else:
        target_unit = my_unit.si_unit

    return my_unit.to_unit(number, target_unit)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    click_convert()
    # x = click_convert(3, 'h', 'minute')
    # print(x)
