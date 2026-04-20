from src.planner import affordability_check, goal_check

def test_planner():
    # Test affordability
    result = affordability_check(40000, 20000, 120000, 50000)
    assert result["affordable"] == True, "Should be affordable"
    
    result = affordability_check(80000, 20000, 120000, 50000)
    assert result["affordable"] == False, "Should not be affordable"
    
    # Test goal
    result = goal_check(70000, 120000, "2026-12-01", 20000)
    assert result["status"] in ["on_track", "behind"], "Status should be valid"
    
    print("Planner tests passed")

if __name__ == "__main__":
    test_planner()