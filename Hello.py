import streamlit as st
from streamlit import session_state as state
import datetime
from pages_ import appointment, appointment_doctor, diet, diet_doctor, exercise, exercise_doctor, info
from persist import persist, load_widget_state


# Define the login page
def login():
    st.title("HIV Management App")
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")
    if st.button("Login", key="login_button"):
        if username == 'user1' and password == "a":
            st.success("Logged in!")
            state.current_user = username
            return True
        elif username == 'user2' and password == 'a':
            st.success("Logged in!")
            state.current_user = username
            return True
        elif username == 'admin' and password == 'a':
            st.success("Logged in!")
            state.current_user = username
            return True
        else:
            st.error("Invalid username or password.")
            return False

# Define the main function
def main():
    if 'passed_login' not in state:
        state.passed_login = False
    if not state.passed_login:
        if not login():
            return
        state.passed_login = True
    pages = {
        'Appointment': appointment.main,
        'Appointment Doctor': appointment_doctor.main,
        'Diet': diet.main,
        'Diet Doctor': diet_doctor.main,
        'Exercise': exercise.main,
        'Exercise Doctor': exercise_doctor.main,
        'Info': info.main
    }
    st.sidebar.title('All Pages')
    page = st.sidebar.selectbox('Select Page', tuple(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    load_widget_state()
    main()
