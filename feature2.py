# feature2.py

def generate_summary(df):
    """
    Generates a summary of total income, total expenses, net balance, and category-based breakdown.
    
    Parameters:
    - df (DataFrame): The DataFrame containing financial entries.
    
    Returns:
    - summary (dict): A dictionary with total income, total expenses, net balance, and category breakdown.
    It also prints the summary to the console.
    """
    total_income = df[df["type"] == "income"]["amount"].sum()
    total_expense = df[df["type"] == "expense"]["amount"].sum()
    net_balance = total_income - total_expense
    
    category_expense = df[df["type"] == "expense"].groupby("category")["amount"].sum()
    category_income = df[df["type"] == "income"].groupby("category")["amount"].sum()

    print("\n--- Monthly Summary ---")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expense}")
    print(f"Net Balance: ${net_balance}")
    
    print("\n--- Expenses by Category ---")
    print(category_expense.to_string())
    
    print("\n--- Income by Category ---")
    print(category_income.to_string())

    summary = {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance,
        "category_expense": category_expense.to_dict(),
        "category_income": category_income.to_dict()
    }
    
    return summary    
    



