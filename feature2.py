# feature2.py

def generate_summary(df):
    """
    Generates a summary of total income, total expenses, and net balance.
    
    Parameters:
    - df (DataFrame): The DataFrame containing financial entries.
    
    Returns:
    - summary (dict): A dictionary with total income, total expenses, and net balance.
    It also prints the summary to the console.
    """
    total_income = df[df["type"] == "income"]["amount"].sum()

    total_expense = df[df["type"] == "expense"]["amount"].sum()

    net_balance = total_income - total_expense

    print("\n--- Monthly Summary ---")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expense}")
    print(f"Net Balance: ${net_balance}")

    summary = {"total_income": total_income,"total_expense": total_expense, "net_balance": net_balance}
    
    return summary
