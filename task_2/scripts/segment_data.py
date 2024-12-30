import pandas as pd

def segment_data(data, feature, group_a_value, group_b_value):
    """
    Segments data into Group A (control) and Group B (test).
    :param data: DataFrame containing the data.
    :param feature: The column to segment by.
    :param group_a_value: Value representing Group A.
    :param group_b_value: Value representing Group B.
    :return: Group A DataFrame, Group B DataFrame
    """
    group_a = data[data[feature] == group_a_value]
    group_b = data[data[feature] == group_b_value]
    return group_a, group_b
