import streamlit as st
import random
from backend import convert_value, list_quantities, list_units

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "First"

# Navigation buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("First"):
        st.session_state.page = "First"
with col2:
    if st.button("Graph"):
        st.session_state.page = "Graph"
with col3:
    if st.button("Password Checker"):
        st.session_state.page = "Password Checker"
with col4:
    if st.button("Unit Converter"):
        st.session_state.page = "Unit Converter"

# Sidebar only for Unit Converter
if st.session_state.page == "Unit Converter":
    quantity = st.sidebar.radio("Select a quantity", list_quantities())

st.divider()

# Pages
if st.session_state.page == "First":
    st.title("🎈 My new app")
    st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

elif st.session_state.page == "Graph":
    st.title("Die Roll simulator")
    num_rolls = st.slider('Number of die rolls', min_value=10, max_value=50)
    if st.button('Plot Graph'):
        die_rolls = [random.randint(1,6) for _ in range(num_rolls)]
        st.line_chart(data=die_rolls)

elif st.session_state.page == "Password Checker":
    conditions = {
        'More than 8 characters': lambda pw: len(pw) > 8,
        'At least 1 uppercase': lambda pw: any(char.isupper() for char in pw),
        'At least 1 lowercase': lambda pw: any(char.islower() for char in pw),
        'At least 1 special character': lambda pw: any(char in ",.!@#$%^&*()" for char in pw),
    }

    def get_password_properties(password):
        return {cond: check(password) for cond, check in conditions.items()}
    
    st.title("Password checker")
    password_input = st.text_input("enter your password", type="password")
    if st.button("check password!"):
        properties = get_password_properties(password_input)
        for condition, passes in properties.items():
            if passes:
                st.success(f'Pass: {condition}')
            else:
                st.error(f'Fail: {condition}')

elif st.session_state.page == "Unit Converter":
    st.title("Unit converter")
    input_num = st.text_input("Value to convert", value="0")
    units = list_units(quantity)
    from_unit = st.selectbox("From", units)
    to_units = st.selectbox("To", units, index=1)