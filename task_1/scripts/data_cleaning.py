import pandas as pd
from scipy.stats import mstats

def drop_high_missing_columns(data, threshold=0.8):
    """Drops columns with missing values above a specified threshold."""
    return data.loc[:, data.isnull().mean() < threshold]

def fill_missing_values(data):
    """Fills missing values in numerical and categorical columns."""
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns

    for col in categorical_cols:
        data[col].fillna(data[col].mode()[0], inplace=True)

    for col in numerical_cols:
        data[col].fillna(data[col].median(), inplace=True)

    return data

def standardize_formats(data):
    """Standardizes date and categorical formats."""
    if 'TransactionMonth' in data.columns:
        data['TransactionMonth'] = pd.to_datetime(data['TransactionMonth'])

    categorical_cols = data.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        data[col] = data[col].astype('category')

    return data

def handle_outliers(data):
    """Removes or caps outliers."""
    data = data[(data['TotalPremium'] >= 0) & (data['TotalClaims'] >= 0)]
    data['TotalPremium'] = mstats.winsorize(data['TotalPremium'], limits=[0.01, 0.01])
    return data

def drop_constant_columns(data):
    """Drops columns with only one unique value."""
    constant_cols = [col for col in data.columns if data[col].nunique() == 1]
    data.drop(columns=constant_cols, inplace=True)
    return data
