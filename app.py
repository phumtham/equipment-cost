
import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("ค่าอุปกรณ์.xlsx", engine="openpyxl")

# Rename columns for easier access
df.columns = ["Equipment", "Code", "Cost", "Universal Healthcare", "UCEP", "Social Security", "Civil Service", "Self Pay"]

# Map scheme names to column names
scheme_map = {
    "Universal Healthcare": "Universal Healthcare",
    "UCEP": "UCEP",
    "Social Security": "Social Security",
    "Civil Service": "Civil Service",
    "Self Pay": "Self Pay"
}

# Streamlit app interface
st.title("Operation Equipment Cost Calculator")

# Select healthcare scheme
selected_scheme = st.selectbox("Select Healthcare Scheme", list(scheme_map.keys()))

st.write("Enter the quantity of each equipment used in the operation:")

# Input quantities for each equipment
quantities = {}
for index, row in df.iterrows():
    qty = st.number_input(f"{row['Equipment']} (Cost: {row['Cost']} THB)", min_value=0, step=1, key=row['Equipment'])
    quantities[row['Equipment']] = qty

# Calculate totals
total_cost = 0
total_reimbursement = 0

for index, row in df.iterrows():
    qty = quantities[row['Equipment']]
    cost = row['Cost'] * qty
    reimbursement = row[scheme_map[selected_scheme]] * qty
    total_cost += cost
    total_reimbursement += reimbursement

out_of_pocket = total_cost - total_reimbursement

# Display results
st.subheader("Summary")
st.write(f"**Total Equipment Cost:** {total_cost:,.2f} THB")
st.write(f"**Total Reimbursement ({selected_scheme}):** {total_reimbursement:,.2f} THB")
st.write(f"**Patient's Out-of-Pocket Expense:** {out_of_pocket:,.2f} THB")
        