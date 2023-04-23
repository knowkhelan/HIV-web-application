import streamlit as st
import sqlite3
import pandas as pd
from streamlit import session_state as state

# state.current_user IS THE USERNAME

# Connect to the SQLite3 database
conn = sqlite3.connect('appointments.db', check_same_thread=False)
c = conn.cursor()

# Create the appointments table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS appointments
             (id INTEGER PRIMARY KEY AUTOINCREMENT, patient_name TEXT, doctor_name TEXT, room_number TEXT, date TEXT, time TEXT, notes TEXT)''')

# Define the appointment scheduling function
def appointment_scheduling():
    st.title("Appointment Scheduling")
    if state.current_user == 'user1' or state.current_user == 'user2':
        patient_name = st.text_input("Patient Name", value=state.current_user)
    else:
        patient_name = st.text_input("Patient Name")
    doctor_name = st.text_input("Doctor Name")
    room_number = st.text_input("Room Number")
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    time_str = appointment_time.strftime('%H:%M:%S')
    notes = st.text_input("Notes")
    if st.button("Schedule Appointment"):
        # Insert the data into the appointments table
        c.execute("INSERT INTO appointments (patient_name, doctor_name, room_number, date, time, notes) VALUES (?, ?, ?, ?, ?, ?)", (patient_name, doctor_name, room_number, appointment_date, time_str, notes))
        conn.commit()
        st.success("Appointment scheduled!")

# Define a function to retrieve appointments from the database
def get_appointments():
    c.execute("SELECT * FROM appointments WHERE patient_name=?", (state.current_user, ))
    appointments = c.fetchall()
    return appointments

# Define a function to clear all appointments from the database
def clear_appointments():
    c.execute("DELETE FROM appointments")
    conn.commit()
    st.success("All appointments cleared!")

# Define the main function
def main():
    appointment_scheduling()
    appointments = get_appointments()

    df = pd.DataFrame(appointments, columns=["ID", "Patient Name", "Doctor Name", "Room Number", "Date", "Time", "Notes"])
    st.dataframe(df)

    if st.button("Clear all appointments"):
        clear_appointments()

if __name__ == '__main__':
    main()
