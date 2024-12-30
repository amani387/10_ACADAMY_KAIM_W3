import pandas as pd
from scipy.stats import chi2_contingency

def chi_squared_test(data, feature, outcome):
    """
    Conducts a Chi-Squared Test on categorical data.
    :param data: DataFrame containing the data.
    :param feature: The feature to test (e.g., 'province').
    :param outcome: The categorical outcome (e.g., 'claims').
    :return: p-value
    """
    contingency_table = pd.crosstab(data[feature], data[outcome])
    chi2, p, _, _ = chi2_contingency(contingency_table)
    return p
