import streamlit as st
import random

tab1, tab2, tab3 = st.tabs(["First", "Second","Third"])
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

