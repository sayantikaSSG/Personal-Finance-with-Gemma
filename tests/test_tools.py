from src.tools import analyze_spending, affordability_check_tool

def test_tools():
    result = analyze_spending()
    assert "total_expenses" in result, "Should have total_expenses"
    
    result = affordability_check_tool(40000)
    assert "affordable" in result, "Should have affordable key"
    
    print("Tools tests passed")

if __name__ == "__main__":
    test_tools()