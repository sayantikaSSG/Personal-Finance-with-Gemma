from datetime import datetime
import json

def load_user_profile(file_path):
    """
    Load user profile from JSON.
    """
    with open(file_path, 'r') as f:
        profile = json.load(f)
    return profile

def affordability_check(cost, monthly_surplus, current_savings, min_buffer=50000):
    """
    Check if a purchase is affordable.
    """
    post_purchase_savings = current_savings - cost
    if post_purchase_savings < min_buffer:
        return {
            "affordable": False,
            "post_purchase_savings": post_purchase_savings,
            "message": f"Purchase would leave savings below buffer of {min_buffer}"
        }
    else:
        return {
            "affordable": True,
            "post_purchase_savings": post_purchase_savings,
            "message": "Purchase is affordable"
        }

def goal_check(goal_amount, current_savings, deadline, monthly_surplus):
    """
    Check progress towards a savings goal.
    """
    deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
    today = datetime.now()
    months_left = (deadline_date.year - today.year) * 12 + (deadline_date.month - today.month)
    if months_left <= 0:
        months_left = 1  # At least 1 month
    
    remaining = goal_amount - current_savings
    required_monthly = remaining / months_left if remaining > 0 else 0
    
    status = "on_track" if monthly_surplus >= required_monthly else "behind"
    
    return {
        "goal_amount": goal_amount,
        "current_savings": current_savings,
        "remaining": max(0, remaining),
        "months_left": months_left,
        "required_monthly": required_monthly,
        "current_monthly_surplus": monthly_surplus,
        "status": status,
        "message": f"You need to save {required_monthly:.0f} per month. Current surplus: {monthly_surplus}"
    }

def suggest_cuts(df, target_extra_savings):
    """
    Suggest spending cuts to achieve target extra savings.
    """
    breakdown = {}
    for category in df['category'].unique():
        cat_exp = abs(df[(df['type'] == 'expense') & (df['category'] == category)]['amount'].sum())
        breakdown[category] = cat_exp
    
    # Sort by highest spend
    sorted_cats = sorted(breakdown.items(), key=lambda x: x[1], reverse=True)
    
    suggestions = []
    total_suggested = 0
    for cat, spend in sorted_cats:
        if total_suggested >= target_extra_savings:
            break
        cut = min(spend * 0.2, target_extra_savings - total_suggested)  # Suggest 20% cut or what's needed
        suggestions.append({"category": cat, "suggested_cut": cut})
        total_suggested += cut
    
    return {
        "target_extra_savings": target_extra_savings,
        "suggested_cuts": suggestions,
        "total_suggested": total_suggested
    }

def recommended_budget_split(salary, fixed_expenses, variable_expenses):
    """
    Recommend a budget split.
    Simple rule: 50% needs, 30% wants, 20% savings.
    """
    total_expenses = fixed_expenses + variable_expenses
    needs = fixed_expenses + variable_expenses * 0.5  # Assume half variable are needs
    wants = variable_expenses * 0.3
    savings = salary - total_expenses
    
    return {
        "needs": needs,
        "wants": wants,
        "savings": savings,
        "recommendation": "Aim for 50% needs, 30% wants, 20% savings"
    }