import json
from pathlib import Path

def load_category_rules(file_path):
    """
    Load category rules from JSON file.
    """
    with open(file_path, 'r') as f:
        rules = json.load(f)
    return rules

def categorize_by_rules(description, rules):
    """
    Categorize a description based on keyword rules.
    """
    desc_lower = description.lower()
    for keyword, category in rules.items():
        if keyword.lower() in desc_lower:
            return category
    return "Other"

def apply_categorization(df, rules_file):
    """
    Apply categorization to the DataFrame using rules, fallback to 'Other'.
    """
    rules = load_category_rules(rules_file)
    df = df.copy()
    df['category'] = df['description'].apply(lambda desc: categorize_by_rules(desc, rules))
    return df