import streamlit as st
import tools
def run():
    st.title("Personalization Page")
    st.write("Please fill in your personal details.")

    # Field: Country
    country = st.text_input("Country", "")

    # Field: City
    city = st.text_input("City", "")

    # Field: Marriage status
    marriage_status_options = ['Single', 'Married', 'Divorced', 'Widowed', 'Other']
    marriage_status = st.selectbox("Marriage Status", marriage_status_options)

    # Field: Number of children
    num_children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)

    # Field: Spending type
    spending_type_options = ['Frugal', 'Big Spender']
    spending_type = st.selectbox("Spending Type", spending_type_options)

    # Field: Monthly Income
    monthly_income = st.number_input("Monthly Income (in IDR)", min_value=0, step=100)

    st.button("Submit",on_click=tools.change_page('expense_page'))