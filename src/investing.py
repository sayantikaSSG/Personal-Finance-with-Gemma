def estimate_investable_surplus(monthly_surplus, emergency_fund_gap):
    """
    Estimate how much surplus can be invested after emergency fund.
    """
    if emergency_fund_gap > 0:
        investable = max(0, monthly_surplus - emergency_fund_gap / 12)  # Spread gap over months
    else:
        investable = monthly_surplus
    return investable

def recommend_allocation(monthly_surplus, risk_level, goal_horizon):
    """
    Recommend asset allocation based on risk and horizon.
    Simple rules.
    """
    if risk_level == "low":
        equity = 0.3
        debt = 0.6
        cash = 0.1
    elif risk_level == "moderate":
        equity = 0.5
        debt = 0.4
        cash = 0.1
    else:  # high
        equity = 0.7
        debt = 0.2
        cash = 0.1
    
    if goal_horizon < 3:
        # Short term, more conservative
        equity -= 0.2
        cash += 0.2
    
    allocation = {
        "equity": max(0, equity),
        "debt": max(0, debt),
        "cash": max(0, cash)
    }
    
    # Normalize
    total = sum(allocation.values())
    allocation = {k: v/total for k, v in allocation.items()}
    
    monthly_allocation = {k: monthly_surplus * v for k, v in allocation.items()}
    
    return {
        "allocation_percent": allocation,
        "monthly_allocation": monthly_allocation,
        "recommendation": f"Based on {risk_level} risk and {goal_horizon} year horizon"
    }

def project_investment_growth(monthly_investment, years, annual_return=0.07):
    """
    Project future value of monthly investments.
    """
    months = years * 12
    monthly_rate = annual_return / 12
    future_value = monthly_investment * ((1 + monthly_rate)**months - 1) / monthly_rate
    return {
        "monthly_investment": monthly_investment,
        "years": years,
        "annual_return": annual_return,
        "future_value": future_value
    }