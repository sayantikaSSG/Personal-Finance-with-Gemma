import pandas as pd
from datetime import datetime

def get_total_income(df, month=None):
    """
    Get total income, optionally filtered by month (YYYY-MM format).
    """
    df_filtered = df[df['type'] == 'income']
    if month:
        df_filtered = df_filtered[df_filtered['date'].dt.strftime('%Y-%m') == month]
    return df_filtered['amount'].sum()

def get_total_expenses(df, month=None):
    """
    Get total expenses, optionally filtered by month.
    """
    df_filtered = df[df['type'] == 'expense']
    if month:
        df_filtered = df_filtered[df_filtered['date'].dt.strftime('%Y-%m') == month]
    return abs(df_filtered['amount'].sum())  # Expenses are negative, but sum as positive

def get_category_breakdown(df, month=None):
    """
    Get spending breakdown by category, optionally filtered by month.
    """
    df_filtered = df[df['type'] == 'expense']
    if month:
        df_filtered = df_filtered[df_filtered['date'].dt.strftime('%Y-%m') == month]
    breakdown = df_filtered.groupby('category')['amount'].sum().abs().to_dict()
    return breakdown

def get_top_expense_categories(df, n=5):
    """
    Get top n expense categories by total amount.
    """
    breakdown = get_category_breakdown(df)
    sorted_categories = sorted(breakdown.items(), key=lambda x: x[1], reverse=True)
    return sorted_categories[:n]

def get_monthly_surplus(df, salary, fixed_expenses=0):
    """
    Calculate monthly surplus: salary - fixed_expenses - variable_expenses.
    Assumes df is for one month.
    """
    total_expenses = get_total_expenses(df)
    surplus = salary - fixed_expenses - total_expenses
    return surplus

def detect_overspending(df, baseline_months=3):
    """
    Detect overspending by comparing current month to average of previous months.
    Returns a dict with flags.
    """
    # Group by month
    df['month'] = df['date'].dt.strftime('%Y-%m')
    monthly_expenses = df[df['type'] == 'expense'].groupby('month')['amount'].sum().abs()
    
    if len(monthly_expenses) < baseline_months + 1:
        return {"overspending": False, "message": "Not enough data for baseline"}
    
    # Current month is the latest
    current_month = monthly_expenses.index[-1]
    current_expense = monthly_expenses.iloc[-1]
    
    # Baseline average
    baseline_avg = monthly_expenses.iloc[:-1].tail(baseline_months).mean()
    
    # Flag if current > average by 20%
    threshold = baseline_avg * 1.2
    overspending = current_expense > threshold
    
    return {
        "overspending": overspending,
        "current_expense": current_expense,
        "baseline_avg": baseline_avg,
        "threshold": threshold,
        "message": f"Current month expense: {current_expense}, Baseline: {baseline_avg}"
    }