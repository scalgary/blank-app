from dataclasses import dataclass

@dataclass

class Unit:
    abbrev: str
    value_in_std_units: float

if __name__ == "__main__":
    gram = Unit(abbrev='g', value_in_std_units=0.001)
    print(gram.abbrev)   
