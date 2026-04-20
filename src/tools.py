import pandas as pd
from .parser import load_transactions, validate_schema, normalize_columns
from .categorizer import apply_categorization
from .analysis import get_total_expenses, get_category_breakdown, get_monthly_surplus
from .planner import affordability_check, goal_check, suggest_cuts, recommended_budget_split, load_user_profile
from .investing import recommend_allocation
from .forecasting import prepare_monthly_series, forecast_with_baseline

def analyze_spending(month_range=None):
    """
    Analyze spending for a given month range.
    """
    # Load data
    df = load_transactions('data/demo_transactions.csv')
    validate_schema(df)
    df = normalize_columns(df)
    df = apply_categorization(df, 'data/category_rules.json')
    
    if month_range:
        # Assume month_range is 'YYYY-MM'
        df = df[df['date'].dt.strftime('%Y-%m') == month_range]
    
    total_exp = get_total_expenses(df)
    breakdown = get_category_breakdown(df)
    
    return {
        "total_expenses": total_exp,
        "category_breakdown": breakdown,
        "month": month_range
    }

def category_breakdown(month_range=None):
    """
    Get category breakdown.
    """
    return analyze_spending(month_range)["category_breakdown"]

def affordability_check_tool(item_cost, min_buffer=50000):
    """
    Tool for affordability check.
    """
    profile = load_user_profile('data/user_profile.json')
    # Need monthly_surplus, but for simplicity, assume from analysis
    # In real, compute from df
    df = load_transactions('data/demo_transactions.csv')
    validate_schema(df)
    df = normalize_columns(df)
    surplus = get_monthly_surplus(df, profile['monthly_salary'], profile['fixed_expenses'])
    
    return affordability_check(item_cost, surplus, profile['current_savings'], min_buffer)

def goal_check_tool(goal_amount, deadline):
    """
    Tool for goal check.
    """
    profile = load_user_profile('data/user_profile.json')
    df = load_transactions('data/demo_transactions.csv')
    validate_schema(df)
    df = normalize_columns(df)
    surplus = get_monthly_surplus(df, profile['monthly_salary'], profile['fixed_expenses'])
    
    return goal_check(goal_amount, profile['current_savings'], deadline, surplus)

def suggest_cuts_tool(target_extra_savings):
    """
    Tool for suggesting cuts.
    """
    df = load_transactions('data/demo_transactions.csv')
    validate_schema(df)
    df = normalize_columns(df)
    df = apply_categorization(df, 'data/category_rules.json')
    
    return suggest_cuts(df, target_extra_savings)

def recommend_allocation_tool():
    """
    Tool for allocation recommendation.
    """
    profile = load_user_profile('data/user_profile.json')
    df = load_transactions('data/demo_transactions.csv')
    validate_schema(df)
    df = normalize_columns(df)
    surplus = get_monthly_surplus(df, profile['monthly_salary'], profile['fixed_expenses'])
    
    # Goal horizon: from deadline
    deadline_date = pd.to_datetime(profile['goal_deadline'])
    today = pd.Timestamp.now()
    horizon = (deadline_date - today).days / 365
    
    return recommend_allocation(surplus, profile['risk_level'], horizon)

def forecast_spending(category=None, months=3):
    """
    Tool for forecasting spending.
    """
    df = load_transactions('data/demo_transactions.csv')
    validate_schema(df)
    df = normalize_columns(df)
    df = apply_categorization(df, 'data/category_rules.json')
    
    series = prepare_monthly_series(df, category)
    forecast = forecast_with_baseline(series, months)
    
    return {
        "category": category,
        "forecast": forecast,
        "months": months
    }