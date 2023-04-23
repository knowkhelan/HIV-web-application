import streamlit as st
import sqlite3
import pandas as pd
from streamlit import session_state as state

# state.current_user IS THE USERNAME

# Connect to the SQLite3 database
conn = sqlite3.connect('exercise.db', check_same_thread=False)
c = conn.cursor()

# Create the exercises table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS exercises
             (id INTEGER PRIMARY KEY AUTOINCREMENT, patient_name TEXT, exercise_name TEXT, duration INTEGER, calories_burnt INTEGER, date TEXT, time TEXT)''')

# Define the exercise logging function
def log_exercise():
    st.title("Exercise Logging")
    if state.current_user == 'user1' or state.current_user == 'user2':
        patient_name = st.text_input("Patient Name", value=state.current_user)
    else:
        patient_name = st.text_input("Patient Name")
    exercise_name = st.text_input("Exercise Name")
    duration = st.number_input("Duration (minutes)")
    calories_burnt = st.number_input("Calories Burnt")
    exercise_date = st.date_input("Exercise Date")
    exercise_time = st.time_input("Exercise Time")
    time_str = exercise_time.strftime('%H:%M:%S')
    if st.button("Log Exercise"):
        # Insert the data into the exercises table
        c.execute("INSERT INTO exercises (patient_name, exercise_name, duration, calories_burnt, date, time) VALUES (?, ?, ?, ?, ?, ?)", (patient_name, exercise_name, duration, calories_burnt, exercise_date, time_str))
        conn.commit()
        st.success("Exercise logged!")

# Define a function to retrieve exercises for a patient from the database
def get_exercises():
    c.execute("SELECT * FROM exercises WHERE patient_name=?", (state.current_user, ))
    exercises = c.fetchall()
    return exercises

# Define the main function
def main():
    log_exercise()
    exercises = get_exercises()

    df = pd.DataFrame(exercises, columns=["ID", "Patient Name", "Exercise Name", "Duration (mins)", "Calories Burnt", "Date", "Time"])
    st.dataframe(df)

    if st.button("Clear all exercises"):
        c.execute("DELETE FROM exercises")
        conn.commit()
        st.success("All exercises cleared!")

if __name__ == '__main__':
    main()
