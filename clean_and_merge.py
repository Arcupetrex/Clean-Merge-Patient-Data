import pandas as pd

# ------------------------------
# Step 1: Load the CSV files
# ------------------------------
# patients1.csv contains: patient_id, name, birthdate
# patients2.csv contains: patient_id, blood_pressure, glucose
df1 = pd.read_csv("patients1.csv")
df2 = pd.read_csv("patients2.csv")

# ------------------------------
# Step 2: Remove duplicates
# ------------------------------
# Remove any duplicate rows based on patient_id from each dataframe
df1 = df1.drop_duplicates(subset="patient_id")
df2 = df2.drop_duplicates(subset="patient_id")

# ------------------------------
# Step 3: Fix date formats
# ------------------------------
# Convert the 'birthdate' column to a standard date format (YYYY-MM-DD)
# Errors are coerced to NaT (Not a Time) if any bad values exist.
df1['birthdate'] = pd.to_datetime(df1['birthdate'], errors='coerce').dt.strftime('%Y-%m-%d')

# ------------------------------
# Step 4: Merge the DataFrames
# ------------------------------
# Merge the two dataframes on the common column 'patient_id'
merged_df = pd.merge(df1, df2, on="patient_id", how="inner")

# ------------------------------
# Step 5: Save and display the merged data
# ------------------------------
# Save the cleaned and merged data to a new CSV file
merged_df.to_csv("merged_patients.csv", index=False)

# Print the first few rows of the merged dataframe for verification
print(merged_df.head())
