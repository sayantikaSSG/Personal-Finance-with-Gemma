# Utility functions

def format_currency(amount):
    return f"₹{amount:,.0f}"

def calculate_months_left(deadline):
    from datetime import datetime
    deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
    today = datetime.now()
    return max(1, (deadline_date.year - today.year) * 12 + (deadline_date.month - today.month))