import streamlit as st
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

st.write("""
# The Pomodoro App

Let's do some focus work in data science with this app.
""")

selected_time = st.selectbox("Select time duration for Pomodoro session:", [1, 5, 10, 15, 20, 25, 30])
selected_time_seconds = selected_time * 60

button_clicked = st.button("Start", key="start_button")

if button_clicked:
    with st.empty():
        while selected_time_seconds:
            mins, secs = divmod(selected_time_seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            selected_time_seconds -= 1
            st.success(f"🔔 {selected_time} minutes is over! Time for a break!")

    st.success("Pomodoro session finished!")
