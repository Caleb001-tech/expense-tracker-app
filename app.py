import streamlit as st
import json
from datetime import date

data_file = "expenses.json"
def load_expense():
    with open(data_file, "r") as file:
        return json.load(file)

def save_expense(expenses):
    with open(data_file, "w") as file:
        json.dump(expenses, file)
def add_expense(amount, category, expense_date, note):
    expenses = load_expense()
    new_expense = {
        "amount": amount,
        "category": category,
        "expense_date": str(expense_date),
        "note": note
    }
    expenses.append(new_expense)
    save_expense(expenses)
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total
def filter_by_category(expenses, category):
    filtered = []
    for expense in expenses:
        if expense["category"] == category:
            filtered.append(expense)
    return filtered


st.title("💰💰personal expense tracker")
menu = st.sidebar.radio("menu", ["add expenses", "view expenses", "summary"])
expenses = load_expense()
if menu == "add expenses":
    st.header("Add new expenses")
    amount = st.number_input("Enter Amount", min_value=0.0)
    category = st.selectbox("Select Category", ["food", "transport", "bills", "shopping", "others"])
    expense_date = st.date_input("select date", date.today())
    note = st.text_input("Enter Note(optional)")
    if st.button("add expenses"):
     if amount > 0:
        add_expense(amount, category, expense_date, note)
        st.success("expense added successfully")
     else:
        st.error("amount cannot be negative")
elif menu == "view expenses":
    st.header("View expenses")
    if len(expenses) == 0:
        st.error("no expenses")
    else:
        st.table(expenses)
elif menu == "summary":
    total = calculate_total(expenses)
    st.subheader(f"Total spending: #{total}")
    categories = set()
    for expense in expenses:
        categories.add(expense["category"])
        selected_category = st.selectbox("filter by category", ["ALL"] + list(categories))
        if selected_category == "ALL":
            filtered_expenses = expenses
        else:
            filtered_expenses = filter_by_category(expenses, selected_category)
            st.table(filtered_expenses)



