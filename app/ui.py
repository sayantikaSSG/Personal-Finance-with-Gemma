import streamlit as st
import pandas as pd
from src.parser import load_transactions, validate_schema, normalize_columns
from src.categorizer import apply_categorization
from src.analysis import get_total_expenses, get_category_breakdown
from app.agents import process_query

def run_ui():
    st.title("Personal Finance Copilot")
    
    # Profile section
    st.header("User Profile")
    profile = {
        "monthly_salary": 80000,
        "fixed_expenses": 25000,
        "current_savings": 120000,
        "goal": "Laptop - 70000 by 2026-12-01"
    }
    st.json(profile)
    
    # Transactions dashboard
    st.header("Transactions Dashboard")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        df = load_transactions('data/demo_transactions.csv')
    
    validate_schema(df)
    df = normalize_columns(df)
    df = apply_categorization(df, 'data/category_rules.json')
    
    st.dataframe(df)
    
    total_exp = get_total_expenses(df)
    st.metric("Total Expenses", f"₹{total_exp}")
    
    breakdown = get_category_breakdown(df)
    st.bar_chart(breakdown)
    
    # Ask assistant
    st.header("Ask the Assistant")
    query = st.text_input("Enter your question")
    if st.button("Ask"):
        result = process_query(query)
        st.json(result)

if __name__ == "__main__":
    run_ui()