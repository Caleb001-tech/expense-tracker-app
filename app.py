import streamlit as st
import json
import os
import uuid
from datetime import date

admin_file = "all_users_expenses.json"
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())
user_id = st.session_state.user_id
data_file = f"expenses_{st.session_state.user_id}.json"
if not os.path.exists(data_file):
    with open(data_file, "w") as f:
        json.dump([], f)


def load_users_expenses():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return []


def save_expense(expenses):
    with open(data_file, "w") as f:
        json.dump(expenses, f, indent=4)
def update_expense(new_expenses):
    all_expenses = []
    if os.path.exists(admin_file):
        with open(admin_file, "r") as f:
            all_expenses = json.load(f)
    all_expenses.append(new_expenses)
    with open(admin_file, "w") as f:
        json.dump(all_expenses, f, indent=4)

def delete_expense(index):
    expenses = load_users_expenses()
    expenses.pop(index)
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


st.title("💰💰CALEB expense tracker")
st.write("This expense tracker app was created by caleb offiong james")
st.write(f"your user id is: {user_id}")
menu = st.sidebar.radio("menu", ["add expenses", "view expenses", "remove expenses", "summary"])
if menu == "add expenses":
    st.header("Add new expenses")
    amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")
    category = st.selectbox("Select Category", ["food", "transport", "bills", "shopping", "housing", "anonymous", "others"], key="category_d")
    expense_date = st.date_input("select date", date.today())
    note = st.text_input("Enter Note(optional)")
    if st.button("add expenses"):
     if amount > 0:
         expense = {
             "amount": amount,
             "category": category,
             "expense_date": str(expense_date),
             "note": note
         }
         user_expenses = load_users_expenses()
         user_expenses.append(expense)
         save_expense(user_expenses)
         update_expense(expense)
         st.success("expense added successfully")
     else:
        st.error("amount cannot be negative")
elif menu == "view expenses":
    st.header("View expenses")
    expenses = load_users_expenses()
    if len(expenses) == 0:
        st.error("no expenses yet")
    else:
        st.table(expenses)
elif menu == "remove expenses":
    expenses = load_users_expenses()
    if len(expenses) == 0:
        st.info("no expenses yet")
    else:
        for i, expense in enumerate(expenses):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{i+1}.{expense['category']} {expense['amount']} {expense['expense_date']}")
            with col2:
                if st.button("Delete", key= f"delete_{i}"):
                    delete_expense(i)
                    st.success("expense removed successfully")
                    st.rerun()


elif menu == "summary":
    expenses = load_users_expenses()
    total = calculate_total(expenses)
    st.subheader(f"Total spending: #{total}")
    categories = set()
    for expense in expenses:
        categories.add(expense["category"])
    selected_category = st.selectbox("select expense category", ["ALL"] + list(categories), key="summary_category_f")
    if selected_category == "ALL":
        filtered_expenses = expenses
    else:
        filtered_expenses = filter_by_category(expenses, selected_category)
        st.table(filtered_expenses)



