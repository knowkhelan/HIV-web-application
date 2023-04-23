import streamlit as st

# Define the information page
def information():
    st.title("Information about HIV")
    st.write("HIV stands for Human Immunodeficiency Virus. It is a virus that attacks the immune system, which is the body's natural defense against illness. Over time, HIV can destroy the immune system, leaving the body vulnerable to infections and diseases.")
    st.write("HIV is primarily spread through sexual contact, sharing needles or syringes, and from mother to child during pregnancy, childbirth, or breastfeeding. HIV can also be transmitted through blood transfusions or organ transplants from an infected donor.")
    st.write("There is currently no cure for HIV, but antiretroviral therapy (ART) can help people with HIV live longer, healthier lives. ART works by stopping the virus from multiplying in the body, which reduces the amount of HIV in the blood and prevents the progression of HIV to AIDS.")
    st.write("It is important to get tested for HIV if you think you may have been exposed. Early diagnosis and treatment can improve outcomes and reduce the risk of transmission to others.")

# Define the main function
def main():
    information()

if __name__ == '__main__':
    main()
