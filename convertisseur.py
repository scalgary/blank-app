
import streamlit as st
import random
from backend import convert_value, list_quantities, list_units



quantity = st.sidebar.radio("Select a quantity", list_quantities())
st.title("Unit Converter")

input_num = float(st.text_input("Value to convert", value = "0"))

units = list_units(quantity)
from_unit_col, to_unit_col = st.columns(2)
with from_unit_col:
    from_unit = st.selectbox("From", units)
with to_unit_col:
    to_unit = st.selectbox("To", units, index=1)
def format_value(
        value: float,
        unit_abbrev: str,
        decimal_places: int = None) -> str:
    is_rounded = decimal_places is not None
    rounded = round(value, decimal_places) if is_rounded else value
    formatted = format(rounded, ",")
    return f"{formatted} {unit_abbrev}"

places = None
if st.checkbox("Round result?", value=False):
    places = st.number_input("Decimal places to round to", value=2, min_value=0)

result = convert_value(quantity, from_unit, to_unit, input_num)

#from_display = f"{result.from_value} {result.from_unit.abbrev}"
from_display = format_value(input_num, result.from_unit.abbrev, places)
#to_display = f"{result.to_value} {result.to_unit.abbrev}"
to_display =format_value(result.to_value,result.to_unit.abbrev, places)
from_value_col, to_value_col = st.columns(2)
from_value_col.metric("From", from_display, delta=None)
to_value_col.metric("To", to_display, delta=None)
