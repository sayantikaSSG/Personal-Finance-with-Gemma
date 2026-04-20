import pandas as pd
import json
from pathlib import Path

def load_transactions(file_path):
    """
    Load transactions from a CSV file into a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def validate_schema(df):
    """
    Validate that the DataFrame has the required columns.
    """
    required_columns = ['date', 'description', 'amount', 'type', 'category']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Missing required columns. Expected: {required_columns}")
    return True

def normalize_columns(df):
    """
    Normalize the DataFrame columns: convert date to datetime, amount to numeric, standardize type.
    """
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['type'] = df['type'].str.lower()
    # Ensure type is 'income' or 'expense'
    df['type'] = df['type'].apply(lambda x: 'income' if x == 'income' else 'expense')
    return df