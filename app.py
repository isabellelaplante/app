import streamlit as st
import pandas as pd

#gives the app a light blue background
st.markdown(
"""
    <style>
        .stApp {
            background-color: #d6eaff; /* light blue */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("College Budgeting Tool")
st.write("Welcome to the College Budgeting Tool! This tool will help you create a budget for your college expenses.")

#month selector
month = st.selectbox(
    "Select Month",
    ["January", "February", "March", "April", "May", "June",
     "July", "August", "September", "October", "November", "December"]
)

#yearly totals by month
if "monthly_totals" not in st.session_state:
    st.session_state.monthly_totals = {m: 0 for m in [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]}

st.header("Monthly Expenses Based Upon Category")
#categories for spending 
Goal_for_SpendingTotal = st.slider("What is your goal for your total monthly spending?", min_value=0, value = 2000)
Groceries = st.number_input("Groceries", min_value=0, max_value = 350, value = 200)
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

#saves the total expenses for the month then updates bar chart
if st.button("Save This Month's Spending"):
    st.session_state.monthly_totals[month] = total_expenses
    st.success(f"Saved spending for {month}!")

#displays the breakdown of expenses by category
st.header("Spending Breakdown by Category")
data = {
    "Category": ["Groceries", "Going Out", "Gas", "Entertainment", "School Supplies", "Rent", "Personal Care", "Other"],
    "Amount": [Groceries, Going_Out, Gas, Entertainment, school_supplies, Rent, Personal_Care, Other]
}
df = pd.DataFrame(data)
st.write(df)

#budget analysis and feedback based on remaining budget
st.header("Budget Analysis") 
st.write(f"Your total monthly expenses are: ${total_expenses:.2f}")
st.write(f"Your remaining budget is: ${remaining_budget:.2f}")

if remaining_budget > 200:
    st.success("Great job! You are within your budget. Keep up the good work!")
elif remaining_budget > 0 and remaining_budget <= 200:
        st.warning("You are close to your budget limit. Consider reviewing your expenses to ensure you stay within your goal.")
else:
    if total_expenses > Goal_for_SpendingTotal:
        st.error("Your total expenses exceed your goal for monthly spending. Consider reducing some of your expenses.")

#yearly spending overview with a bar chart to visualize the total spending for each month
st.header("Yearly Spending Overview")

df_year = pd.DataFrame({
    "Month": list(st.session_state.monthly_totals.keys()),
    "Total Spending": list(st.session_state.monthly_totals.values())
})

month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
#streamlit was doing it by alphabetical order, so I had to specify the order of the months to make it look right on the bar chart
df_year["Month"] = pd.Categorical(df_year["Month"], categories=month_order, ordered=True)
df_year = df_year.sort_values("Month")

st.bar_chart(df_year, x="Month", y="Total Spending")

