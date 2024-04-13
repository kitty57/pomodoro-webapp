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
stop_button_clicked = False

if button_clicked:
    start_container = st.empty()
    stop_container = st.empty()
    
    with start_container:
        while selected_time_seconds and not stop_button_clicked:
            mins, secs = divmod(selected_time_seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            selected_time_seconds -= 1
            st.success(f"🔔 {selected_time} minutes is over! Time for a break!")
            if st.checkbox("Stop", key="stop_checkbox"):
                stop_button_clicked = True
    
    break_time = 5 * 60
    with stop_container:
        while break_time and not stop_button_clicked:
            mins, secs = divmod(break_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            break_time -= 1
            st.error("⏰ 5 minute break is over!")
            if st.checkbox("I don't want break", key="stop_checkbox_break"):
                stop_button_clicked = True
