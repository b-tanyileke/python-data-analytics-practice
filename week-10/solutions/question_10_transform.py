"""Question 10 sample solution."""
import pandas as pd


def department_report(frame):
    """Standardize department names and rename the report columns."""
    result = frame.loc[:, ["dept", "hours"]].copy()
    result["hours"] = result["hours"].replace("N/A", float("nan"))
    result["dept"] = result["dept"].map({"IT": "Technology", "HR": "Human Resources"})
    return result.rename(columns={"dept": "department", "hours": "hours_worked"})
