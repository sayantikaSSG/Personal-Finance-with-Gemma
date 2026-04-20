from mcp import Tool
from mcp.server import Server
from src.tools import analyze_spending, category_breakdown, affordability_check_tool, goal_check_tool, suggest_cuts_tool, recommend_allocation_tool, forecast_spending

app = Server("finance-copilot")

@app.tool()
def analyze_spending_tool(month_range: str = None) -> str:
    """
    Analyze spending for a given month range.
    """
    result = analyze_spending(month_range)
    return str(result)

@app.tool()
def category_breakdown_tool(month_range: str = None) -> str:
    """
    Get category breakdown.
    """
    result = category_breakdown(month_range)
    return str(result)

@app.tool()
def affordability_check_tool(item_cost: float, min_buffer: float = 50000) -> str:
    """
    Check if an item is affordable.
    """
    result = affordability_check_tool(item_cost, min_buffer)
    return str(result)

@app.tool()
def goal_check_tool(goal_amount: float, deadline: str) -> str:
    """
    Check progress towards a goal.
    """
    result = goal_check_tool(goal_amount, deadline)
    return str(result)

@app.tool()
def suggest_cuts_tool(target_extra_savings: float) -> str:
    """
    Suggest spending cuts.
    """
    result = suggest_cuts_tool(target_extra_savings)
    return str(result)

@app.tool()
def recommend_allocation_tool() -> str:
    """
    Recommend investment allocation.
    """
    result = recommend_allocation_tool()
    return str(result)

@app.tool()
def forecast_spending_tool(category: str = None, months: int = 3) -> str:
    """
    Forecast spending.
    """
    result = forecast_spending(category, months)
    return str(result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)