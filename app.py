import streamlit as st
 
st.title("College Budgeting Tool")
st.write("Welcome to the College Budgeting Tool! This tool will help you create a budget for your college expenses.")

st.header("Monthly Expenses Based Upon Category")
#categories for spending 
Goal_for_SpendingTotal = st.number_input("What is your goal for your total monthly spending?", min_value=0, value = 2000)
Groceries = st.slider("Groceries", min_value=0, max_value = 350, value = 200)
Going_Out = st.number_input("Going Out", min_value=0, value = 150)
Gas = st.number_input("Gas", min_value=0, value = 100)
Entertainment = st.number_input("Entertainment", min_value = 0, value = 100)
school_supplies = st.number_input("School Supplies", min_value = 0, value = 50)
Rent = st.number_input("Rent", min_value = 0, value = 1500)
Personal_Care = st.number_input("Personal Care", min_value = 0, value = 25)
Other = st.number_input("Other", min_value = 0, value = 50)

#calculates total expenses and remaining budget
total_expenses = Groceries + Going_Out + Gas + Entertainment + school_supplies + Rent + Personal_Care + Other
remaining_budget = Goal_for_SpendingTotal - total_expenses


st.header("Budget Analysis") #summary
st.write(f"Your total monthly expenses are: ${total_expenses:.2f}")
st.write(f"Your remaining budget is: ${remaining_budget:.2f}")

if remaining_budget > 200:
    st.success("Great job! You are within your budget. Keep up the good work!")
elif remaining_budget > 0 and remaining_budget <= 200:
        st.warning("You are close to your budget limit. Consider reviewing your expenses to ensure you stay within your goal.")
else:
    if total_expenses > Goal_for_SpendingTotal:
        st.error("Your total expenses exceed your goal for monthly spending. Consider reducing some of your expenses.")
