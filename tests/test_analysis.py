import pandas as pd
from src.parser import load_transactions, validate_schema, normalize_columns
from src.categorizer import apply_categorization
from src.analysis import get_total_expenses, get_category_breakdown, get_monthly_surplus

def test_analysis():
    df = load_transactions('data/demo_transactions.csv')
    validate_schema(df)
    df = normalize_columns(df)
    df = apply_categorization(df, 'data/category_rules.json')
    
    total_exp = get_total_expenses(df)
    assert total_exp > 0, "Total expenses should be positive"
    
    breakdown = get_category_breakdown(df)
    assert isinstance(breakdown, dict), "Breakdown should be dict"
    
    surplus = get_monthly_surplus(df, 80000, 25000)
    assert surplus == 80000 - 25000 - total_exp, "Surplus calculation incorrect"
    
    print("Analysis tests passed")

if __name__ == "__main__":
    test_analysis()