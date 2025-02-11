
# Patient Data Cleaning and Merging Project

This project contains a Python script that cleans and merges two CSV files containing patient data. The first CSV file (`patients1.csv`) includes patient demographics (patient_id, name, birthdate), and the second CSV file (`patients2.csv`) includes clinical measurements (patient_id, blood_pressure, glucose). The script removes duplicates, standardizes date formats, and merges the two files by `patient_id`.

---

## Project Structure

```
.
├── patients1.csv         # Contains: patient_id, name, birthdate
├── patients2.csv         # Contains: patient_id, blood_pressure, glucose
├── clean_and_merge.py    # Python script to clean and merge the CSV files
├── merged_patients.csv   # Output file after merging the data
└── README.md             # This file
```

---

## Prerequisites

- Python 3.x
- [Pandas](https://pandas.pydata.org/)

Install the required library using pip:

```bash
pip install pandas
```

---

## How to Run the Script

1. **Place the CSV Files:**  
   Ensure that `patients1.csv` and `patients2.csv` are in the same directory as `clean_and_merge.py`.

2. **Run the Python Script:**  
   Open your terminal or command prompt, navigate to the project directory, and run:

   ```bash
   python clean_and_merge.py
   ```

3. **Output:**  
   The script will:
   - Load the two CSV files.
   - Remove duplicate rows based on `patient_id`.
   - Standardize the `birthdate` column to the format `YYYY-MM-DD`.
   - Merge the datasets on `patient_id`.
   - Save the merged dataset to a file named `merged_patients.csv`.

---

## CSV File Details

### patients1.csv
- **Columns:** `patient_id`, `name`, `birthdate`  
- **Description:** Contains demographic data with real Arabic names from Egypt.

### patients2.csv
- **Columns:** `patient_id`, `blood_pressure`, `glucose`  
- **Description:** Contains clinical measurement data.

---

## Script Overview

The script (`clean_and_merge.py`) performs the following steps:
- **Load Data:** Reads both CSV files into Pandas DataFrames.
- **Remove Duplicates:** Eliminates duplicate rows based on the `patient_id`.
- **Fix Date Formats:** Converts the `birthdate` field to a standardized date format (`YYYY-MM-DD`).
- **Merge Data:** Joins the two DataFrames on `patient_id` using an inner join.
- **Save Output:** Writes the merged DataFrame to `merged_patients.csv` for further use.

---

## License

This project is open source and available under the MIT License.

---

## Contributing

Contributions, suggestions, and improvements are welcome!  
Feel free to fork the repository and submit a pull request.

---

## Contact

For any questions or feedback, please contact [Sheref Saadia] via [https://github.com/Arcupetrex].
```