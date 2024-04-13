import streamlit as st
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")
st.title("The Pomodoro App")
st.caption("""
Helps you to focus and concentrate!!!
""")

selected_time = st.selectbox("Select time duration for Pomodoro session (in minutes):", [1, 5, 10, 15, 20, 25, 30])
selected_time_seconds = selected_time * 60

button_clicked = st.button("Start", key="start_button")
stop_checkbox = st.checkbox("Stop", key="stop_checkbox")
stop_button_clicked = False

if button_clicked:
    start_container = st.empty()
    
    with start_container:
        while selected_time_seconds and not stop_button_clicked and not stop_checkbox:
            mins, secs = divmod(selected_time_seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            selected_time_seconds -= 1
            if stop_checkbox:
                stop_button_clicked = True
                st.error("You gave up!")
        
        if not stop_button_clicked and not stop_checkbox:
            st.success(f"🔔 {selected_time} minutes is over! Time for a break!")
            time.sleep(2)  # Wait for 2 seconds before starting the break timer
            
            break_time = 5 * 60  # 5 minutes break time
            while break_time and not stop_button_clicked:
                mins, secs = divmod(break_time, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                st.header(f"⏳ {timer}")
                time.sleep(1)
                break_time -= 1
            
            if not stop_button_clicked:
                st.error("⏰ 5 minute break is over!")
                time.sleep(2)  # Wait for 2 seconds before allowing to start another Pomodoro session

        
