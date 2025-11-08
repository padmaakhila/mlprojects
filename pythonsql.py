import pandas as pd
import pyodbc
df = pd.read_csv(r"C:\Data\retail_sales_datasetss.csv")

# Rename columns to match SQL table exactly
# Rename CSV columns to match SQL table
df.rename(columns={
    'Customer ID': 'CustomerName',  # This is the key fix
    'Product Category': 'ProductCategory',
    'Price per Unit': 'Price',
    'Total Amount': 'TotalAmount'
}, inplace=True)

# Load your CSV
file_path = r"C:\Data\retail_sales_datasetss.csv"
df = pd.read_csv(file_path)

# Strip spaces from column names (just in case)
df.columns = [c.strip().replace(" ", "") for c in df.columns]

# Convert date column (adjust if your CSV column name is 'Date' or 'date')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=AKHILA\\SQLEXPRESS;"
    "DATABASE=RetailSales;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
print(" Connected to SQL Server!")

# Insert data into table
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO retail_sales (Date, CustomerName, Gender, Age, ProductCategory, Quantity, Price, TotalAmount)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    row['Date'],
    row.get('CustomerName', ''),       # use .get() to avoid KeyError
    row.get('Gender', ''),
    row.get('Age', 0),
    row.get('ProductCategory', ''),
    row.get('Quantity', 0),
    row.get('Price', 0.0),
    row.get('TotalAmount', 0.0)
    )

conn.commit()
print(" All data inserted successfully!")
conn.close()
print(" Connection closed.")
