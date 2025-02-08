import pandas as pd
import re
from fpdf import FPDF

# Full path to the file
file_path = r"C:\Users\ASUS\Downloads\Python Internship\GlobalYouTubeStatistics.csv"

# Load the CSV file
df = pd.read_csv(file_path)

# Strip any leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Replace NaN values with '-'
df = df.fillna('-----')

# Remove rows where any column has a value of 0
df = df[(df != 0).all(axis=1)]

# Filter rows where the title contains only English characters
def is_english(text):
    return bool(re.match(r'^[A-Za-z0-9\s\.,!?\'"-]*$', text))

df_filtered = df[df['Channel Name'].apply(is_english)]  # Apply the filter function to the 'Title' column

# Select relevant columns: Title, Video Views, Category, and Country
df_filtered = df_filtered[['Channel Name', 'Views', 'Category', 'Country']]

# Create a PDF document in landscape mode
pdf = FPDF(orientation='L', unit='mm', format='A4')  # 'L' for Landscape
pdf.add_page()

# Set title with Times New Roman
pdf.set_font("Times", size=16, style='B')
pdf.cell(0, 10, txt="YouTube Channels Statistics Report 2023", ln=True, align="C")

# Add a line break
pdf.ln(10)

# Table Headers
column_names = ['Serial No.', 'Channel Name', 'Views', 'Category', 'Country']
data_columns = ['Channel Name', 'Views', 'Category', 'Country']

# Calculate column widths dynamically
pdf.set_font("Times", size=10)
max_lengths = [len(col) for col in column_names]

# Update max_lengths based on the content of the data
for col, name in zip(data_columns, column_names[1:]):
    max_lengths[column_names.index(name)] = max(max_lengths[column_names.index(name)], *(df_filtered[col].astype(str).str.len()))

# Convert max lengths to column widths
col_widths = [max_length * 2.5 for max_length in max_lengths]

# Add table headers
pdf.set_font("Times", size=12, style='B')
for col_name, col_width in zip(column_names, col_widths):
    pdf.cell(col_width, 10, col_name, border=1, align="C")
pdf.ln()

# Add table data
pdf.set_font("Times", size=10)
for index, row in df_filtered.iterrows():
    pdf.cell(col_widths[0], 10, str(index + 1), border=1, align="C")  # Serial No.
    pdf.cell(col_widths[1], 10, row['Channel Name'], border=1, align="C")  # Title
    pdf.cell(col_widths[2], 10, str(row['Views']), border=1, align="C")  # Video Views
    pdf.cell(col_widths[3], 10, row['Category'], border=1, align="C")  # Category
    pdf.cell(col_widths[4], 10, row['Country'], border=1, align="C")  # Country
    pdf.ln()

# Save the PDF to a specific location
pdf_output_path = r"C:\Users\ASUS\OneDrive\ドキュメント\Reports\Global_YouTube_Statistics_Report_Centered.pdf"
pdf.output(pdf_output_path)

print(f"PDF report saved to: {pdf_output_path}")
