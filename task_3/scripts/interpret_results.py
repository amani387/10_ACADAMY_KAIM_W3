def interpret_results(p_value, alpha=0.05):
    """
    Interprets the results of a statistical test.
    :param p_value: p-value from the test.
    :param alpha: Significance level (default: 0.05).
    :return: Interpretation string.
    """
    if p_value < alpha:
        return "Reject Null Hypothesis: Significant difference detected."
    else:
        return "Fail to Reject Null Hypothesis: No significant difference detected."
