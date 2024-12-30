# Task 3: A/B Hypothesis Testing

## **Objective**
This task involves conducting A/B hypothesis testing to evaluate the impact of various features on key performance indicators (KPIs). The results will guide decision-making regarding significant differences in risk and profit margins across different groups.

## **Null Hypotheses**
1. **Risk Differences Across Provinces**: There are no risk differences across provinces.
2. **Risk Differences Between Zip Codes**: There are no risk differences between zip codes.
3. **Profit Margins Across Zip Codes**: There are no significant margin (profit) differences between zip codes.
4. **Risk Differences Between Genders**: There are no significant risk differences between Women and Men.

---

## **Tasks**

### 1. **Select Metrics**
   - **KPI for Risk**: Claim Frequency (number of claims filed per policyholder) or Loss Ratio (claims paid ÷ premiums collected).
   - **KPI for Profit**: Average profit margin (Premiums collected - Claims paid).

### 2. **Data Segmentation**
   - **Group A (Control Group)**: Plans without the feature being tested.
   - **Group B (Test Group)**: Plans with the feature being tested.
   - For features with more than two categories, choose two groups to compare while ensuring that all other attributes (e.g., demographics, plan type) are statistically equivalent.

### 3. **Statistical Testing**
   - Conduct statistical tests to evaluate differences between the groups:
     - **Chi-squared Test**: For categorical KPIs (e.g., risk occurrence across provinces).
     - **T-Test or Z-Test**: For numerical KPIs (e.g., average profit margins).
     - **ANOVA**: For comparing means across more than two groups.

   - Analyze the **p-value**:
     - If \( p < 0.05 \): Reject the null hypothesis (significant difference exists).
     - If \( p \geq 0.05 \): Fail to reject the null hypothesis (no significant difference).

### 4. **Analyze and Report**
   - Document the statistical outcomes.
   - Highlight whether the null hypotheses were rejected or not.
   - Provide business implications and insights for each result.

---

## **Steps for Implementation**

### 1. **Environment Setup**
   - Merge branches from Task 2 into the `main` branch using a Pull Request (PR).
   - Create a new branch called `task-3`.

### 2. **Data Preparation**
   - Load and preprocess the dataset for segmentation.
   - Verify equivalence of groups using statistical methods.

### 3. **Conduct Statistical Tests**
   - Use appropriate statistical tests for KPIs.
   - Log results and analyze the significance of differences.

### 4. **Reporting**
   - Summarize findings in a well-structured document with:
     - Statistical test results.
     - Business implications.
     - Recommendations for further actions.

---

## **Technical Details**

### Dependencies
The following libraries will be used for data processing and statistical analysis:
- **pandas**: For data manipulation.
- **scipy**: For statistical testing (e.g., chi-squared, t-tests).
- **matplotlib/seaborn**: For visualizing results.

### Sample Code
#### Chi-squared Test Example
```python
from scipy.stats import chi2_contingency
import pandas as pd

# Create a contingency table
data = {'Province A': [30, 70], 'Province B': [50, 50]}
contingency_table = pd.DataFrame(data, index=['No Claim', 'Claim'])

# Conduct Chi-squared Test
chi2, p, dof, expected = chi2_contingency(contingency_table)

if p < 0.05:
    print("Reject Null Hypothesis: Significant risk differences across provinces.")
else:
    print("Fail to Reject Null Hypothesis: No significant risk differences across provinces.")
