import pandas as pd

def initialize_df():
    """
    Initializes an empty DataFrame for tracking financial entries.
    """
    finance_log = pd.DataFrame(columns=["amount", "category", "type"])
    return finance_log

def add_entry(df, amount, category, entry_type="expense"):
    """
    Adds an income or expense entry to the existing DataFrame.
    
    Parameters:
    - df (DataFrame): The DataFrame to add the entry to
    - amount (float): The amount of the entry
    - category (str): Category of the entry 
    - entry_type (str): Type of entry ("income" or "expense") --> Default is set to "expense"
    
    Returns:
    -DataFrame: The updated DataFrame with the new entry added.
    """
    
    if not isinstance(amount, (int, float))
        raise ValueError()

    new_entry = pd.DataFrame([[amount, category, entry_type]], columns=["amount", "category", "type"])
    df = pd.concat([df, new_entry], ignore_index=True)
    print(f"Added {entry_type}: ${amount} in category '{category}'.")
    return df

