from scipy.stats import ttest_ind

def t_test(group_a, group_b, kpi):
    """
    Conducts a T-Test on a numerical KPI.
    :param group_a: DataFrame for Group A.
    :param group_b: DataFrame for Group B.
    :param kpi: The column name of the numerical KPI.
    :return: p-value
    """
    stat, p_value = ttest_ind(group_a[kpi], group_b[kpi], nan_policy='omit')
    return p_value
