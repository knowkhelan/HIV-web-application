import streamlit as st
import sqlite3
import pandas as pd
from streamlit import session_state as state

# state.current_user IS THE USERNAME

# Connect to the SQLite3 database
conn = sqlite3.connect('diet.db', check_same_thread=False)
c = conn.cursor()

# Create the diet table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS diet
             (id INTEGER PRIMARY KEY AUTOINCREMENT, patient_name TEXT, food_name TEXT, calories INT, protein INT, fats INT, carbs INT, date TEXT, time TEXT)''')

# Define the function to log the patient's diet
def log_diet():
    st.title("Log Patient's Diet")
    patient_name = st.text_input("Patient Name")
    food_name = st.text_input("Food Name")
    calories = st.number_input("Calories")
    protein = st.number_input("Protein (in grams)")
    fats = st.number_input("Fats (in grams)")
    carbs = st.number_input("Carbs (in grams)")
    diet_date = st.date_input("Date")
    diet_time = st.time_input("Time")
    time_str = diet_time.strftime('%H:%M:%S')
    if st.button("Log Diet"):
        # Insert the data into the diet table
        c.execute("INSERT INTO diet (patient_name, food_name, calories, protein, fats, carbs, date, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (patient_name, food_name, calories, protein, fats, carbs, diet_date, time_str))
        conn.commit()
        st.success("Diet logged!")

# Define a function to retrieve the patient's diet from the database
def get_diet(patient_name):
    c.execute("SELECT * FROM diet WHERE patient_name=?", (patient_name,))
    diet = c.fetchall()
    return diet

# Define a function to calculate the total calories
def calculate_total_calories(diet):
    total_calories = sum([row[3] for row in diet])
    return total_calories

# Define the main function
def main():

    if state.current_user != 'admin':
        st.text("You dont have access to this page!")

    else:
        log_diet()
        patient_name = st.text_input("Enter patient's name to view their diet:")
        diet = get_diet(patient_name)
        df = pd.DataFrame(diet, columns=["ID", "Patient Name", "Food Name", "Calories", "Protein", "Fats", "Carbs", "Date", "Time"])
        st.dataframe(df)
        total_calories = calculate_total_calories(diet)
        st.write("Total calories:", total_calories)

if __name__ == '__main__':
    main()
