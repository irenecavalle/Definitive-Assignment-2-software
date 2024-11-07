# Initialize an empty dictionary to store financial goals
goals = {}

def set_financial_goal(goal_name, target_amount):
    
    # Sets a financial goal by adding a new entry to the goals dictionary.
    goals[goal_name] = {"target": target_amount, "progress": 0}
    print(f"Goal set: '{goal_name}' with a target of ${target_amount}")

def update_goal_progress(goal_name, amount_saved):
    
    # Updates the progress of a financial goal.
    if goal_name in goals:
        goals[goal_name]["progress"] += amount_saved
        current_progress = goals[goal_name]["progress"]
        target = goals[goal_name]["target"]
        print(f"Progress updated for '{goal_name}': ${current_progress} / ${target}")
    else:
        print(f"Goal '{goal_name}' not found.")

# Example usage
set_financial_goal("Emergency Fund", 1000)
update_goal_progress("Emergency Fund", 200)

# Print the goals dictionary
print("\nGoals Progress:")
print(goals)
