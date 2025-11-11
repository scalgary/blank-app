import streamlit as st
import random

tab1, tab2, tab3, tab4 = st.tabs(["First", "Graph","Password Checker"])
with tab1:
    st.title("🎈 My new app")
    st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

with tab2:
    st.title("Die Roll simulator")
    num_rolls = st.slider('Number of die rolls', min_value=10, max_value=50)
    if st.button('Plot Graph'):
        die_rolls = [random.randint(1,6) for _ in range(num_rolls)]
        st.line_chart(data=die_rolls)

with tab3:
    conditions = {
        'More than 8 characters': lambda pw: len(pw) >8,
        'At least 1 uppercase': lambda pw: any(char.isupper() for char in pw),
        'At least 1 lowercase': lambda pw: any(char.islower() for char in pw),
        'At least 1 special character': lambda pw : any(char in ",.!@#$%^&*()" for char in pw),
    }

    def get_password_properties(password):
        return {cond: check(password) for cond, check in conditions.items()}
    
    st.title("Password checker")
    password_input = st.text_input("enter your password", type = "password")
    if st.button("check password!"):
        properties = get_password_properties(password_input)
        for condition, passes in properties.items():
            if passes:
                st.success(f'Pass: {condition}')
            else:
                st.error(f' Fail : {condition}')
    else:
        st.write("Please enter a password")




