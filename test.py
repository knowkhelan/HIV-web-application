import streamlit as st
import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('hiv.db')
c = conn.cursor()

# Create the exercises table if it doesn't exist
# c.execute('''CREATE TABLE IF NOT EXISTS exercises
   #          (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duration INTEGER, date TEXT)''')

# Define the login page
def login():
    st.title("HIV Management App")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("Logged in!")
            return True
        else:
            st.error("Invalid username or password.")
            return False

# Define the exercise tracking page
def exercise_tracking():
    st.title("Exercise Tracking")
    exercise_name = st.text_input("Exercise Name")
    exercise_duration = st.number_input("Duration (minutes)", min_value=1)
    exercise_date = st.date_input("Date")
    if st.button("Add Exercise"):
        c.execute("INSERT INTO exercises (name, duration, date) VALUES (?, ?, ?)", (exercise_name, exercise_duration, exercise_date))
        conn.commit()
        st.success("Exercise added!")

# Define the main function
def main():
    if not login():
        return
    menu = ["Exercise Tracking", "Appointment Scheduling", "Exercise Information"]
    choice = st.sidebar.selectbox("Select an option", menu)
    if choice == "Exercise Tracking":
        exercise_tracking()
    elif choice == "Appointment Scheduling":
        appointment_scheduling()
    elif choice == "Exercise Information":
        exercise_info()

if __name__ == '__main__':
    main()
