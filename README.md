# AUTOMATED-REPORT-GENERATION

**COMPANY** : CODETECH IT SOLUTIONS

**NAME**: Pankaj Singh

**INTERN ID** : CT12LAA

**DOMAIN** : Python Programmimg

**TASK** : Task 2 :- Automated Report Generation

**BATCH DURATION** : January 10th, 2025 to March 10th, 2025

**MENTOR NAME** : Neela Santhosh Kumar

# DESCRIPTION OF THE TASK PERFORMED : AUTOMATED REPORT GENERATION

Introduction

This report chronicles the journey of completing Task 1 from my internship: “Automated Report Generation.” The task required developing a script that reads data from a dataset, analyzes it, and generates a formatted PDF report using Python libraries such as FPDF or ReportLab. The deliverable included the script and a sample PDF report. This document details every step, challenge, and solution encountered during the task.

1. Understanding the Task Requirements

The task’s objective was to:

Load data from a CSV file.

Perform data preprocessing and analysis.

Generate a structured, formatted PDF report.

Initial Steps:

Identified the dataset: "Global YouTube Statistics-2023."

Reviewed dataset features, including columns like Rank, Title, Subscribers, Video Views, Category, and Country.

Chose to use the FPDF library for its simplicity and flexibility.

2. Dataset Preparation

Loading the Dataset:

The dataset was stored in the path: C:\Users\ASUS\Downloads\Python Internship\GlobalYouTubeStatistics.csv.

Used Pandas to load and preview the dataset with the following script:

import pandas as pd
file_path = r"(Your csv file location)"
df = pd.read_csv(file_path)
print(df.head())

Challenges Encountered:

Unicode Error: Encountered due to the file path’s backslashes. Resolved by using a raw string (r"") or double backslashes.

3. Data Preprocessing

Objectives:

Remove unnecessary or irrelevant columns.

Filter rows with English titles.

Handle missing values (NaN) and rows with zero values.

Steps Taken:

Column Selection: Retained relevant columns:

Rank

Title

Video Views

Country

Category

Filter Rows with English Titles:

Used Python’s str.isascii() method to identify English titles.

Handling Missing Values and Zeroes:

Replaced NaN values with '-'.

Dropped rows where any column contained a 0 value.

Adjust Column Names for Readability:

Standardized column names for better presentation in the report.

4. Generating the PDF Report

Initial PDF Setup:

Used the FPDF library to create a PDF document.

Configured the following parameters:

Page layout: Landscape

Font: Times New Roman

Font size: Adjusted dynamically based on content.

Challenges Encountered:

Wide Content Truncation:

Resolved by switching to landscape orientation.

Dynamic Column Widths:

Implemented automatic column width adjustment using string length.

Sample PDF Generation Script:

from fpdf import FPDF

pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Times", size=12)

Add table header:
pdf.set_fill_color(200, 220, 255)
pdf.cell(20, 10, "Rank", border=1, align="C", fill=True)
pdf.cell(60, 10, "Title", border=1, align="C", fill=True)
pdf.cell(40, 10, "Video Views", border=1, align="C", fill=True)
pdf.cell(40, 10, "Country", border=1, align="C", fill=True)
pdf.cell(60, 10, "Category", border=1, align="C", fill=True)
pdf.ln()

Add rows:
for index, row in df.iterrows():
    pdf.cell(20, 10, str(row['Rank']), border=1, align="C")
    pdf.cell(60, 10, row['Title'], border=1, align="C")
    pdf.cell(40, 10, str(row['Video Views']), border=1, align="C")
    pdf.cell(40, 10, row['Country'], border=1, align="C")
    pdf.cell(60, 10, row['Category'], border=1, align="C")
    pdf.ln()

Save the PDF:
output_path = r"(Location where you want to save report,s PDF)"
pdf.output(output_path)

5. Final Adjustments and Refinements

Column Alignment:

Ensured all text was center-aligned for consistency.

Font Adjustments:

Switched to Times New Roman for a professional look.

Table Centering:

Initially tried to center the table but later removed it based on requirements.

6. Challenges and Solutions

6.1 Errors During File Handling

Issue: FileNotFoundError due to incorrect paths.

Solution: Verified paths using os.path.exists() and ensured proper directory access.

6.2 UnicodeEncodeError

Issue: Certain characters were outside the latin-1 encoding range.

Solution: Used utf-8 encoding in the FPDF library.

6.3 Table Formatting

Issue: Data truncation and poor alignment.

Solution: Adjusted column widths dynamically and used landscape orientation.

7. Final Outcome

A comprehensive, well-formatted PDF report was successfully generated.

The report contained the required data with proper alignment and formatting.

It was saved at the specified path.

8. Key Learnings

Mastery over data handling and preprocessing using Pandas.

Enhanced familiarity with FPDF for generating professional reports.

Improved problem-solving skills by addressing common errors like encoding issues and file path mismatches.

Importance of dynamic adjustments for scalability across various datasets.

Conclusion

The journey to complete this task was both challenging and rewarding. It provided a hands-on opportunity to work with real-world datasets, implement data preprocessing, and generate automated reports. The final script is flexible and can handle various datasets with minimal modifications. This task has laid a strong foundation for further projects in data analysis and reporting.

