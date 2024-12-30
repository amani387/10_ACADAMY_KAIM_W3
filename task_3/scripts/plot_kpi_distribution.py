import seaborn as sns
import matplotlib.pyplot as plt

def plot_kpi_distribution(group_a, group_b, kpi, group_a_label="Group A", group_b_label="Group B"):
    """
    Plots the KPI distribution for both groups.
    :param group_a: DataFrame for Group A.
    :param group_b: DataFrame for Group B.
    :param kpi: The column name of the KPI.
    :param group_a_label: Label for Group A.
    :param group_b_label: Label for Group B.
    """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(group_a[kpi], label=group_a_label, shade=True, color="blue")
    sns.kdeplot(group_b[kpi], label=group_b_label, shade=True, color="orange")
    plt.title(f"Distribution of {kpi}")
    plt.xlabel(kpi)
    plt.ylabel("Density")
    plt.legend()
    plt.show()
