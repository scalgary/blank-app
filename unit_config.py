from typing import Dict
from quantity import Quantity
from unit import Unit

unit_config: Dict[str, Quantity] = {
    "Mass": Quantity(
        std_unit="Kilograms",
            units={
                "Kilograms" : Unit(abbrev="kg", value_in_std_units=1),
                "Grams": Unit(abbrev="g", value_in_std_units=0.001),
                "Pounds": Unit(abbrev="lb", value_in_std_units=0.453592),
                "Ounces": Unit(abbrev="oz", value_in_std_units=0.0283495),

            }
        ),
    "Time": Quantity(
        std_unit="Seconds",
        units={
            "Seconds": Unit(abbrev="s", value_in_std_units=1),
            "Minutes": Unit(abbrev="min", value_in_std_units=60),
            "Hours": Unit(abbrev="hr", value_in_std_units=3600),
            "Days": Unit(abbrev="d", value_in_std_units=86400),
        }
    )
}