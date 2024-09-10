import pandas as pd
from functions import generate_email  # Import the email generation function

def main():
    # Load student data from the Excel file
    df = pd.read_excel(r'C:\Users\Hp\Downloads\Test Files.xlsx')

    # Track existing emails for uniqueness
    existing_emails = set()

    # Generate email addresses for all students
    df['Email Address'] = df['Student Name'].apply(lambda name: generate_email(name, existing_emails))

    # Save the data with email addresses to CSV and TSV files
    df.to_csv('output/students.csv', index=False)
    df.to_csv('output/students.tsv', sep='\t', index=False)

    # Additional steps for shuffling or logging can be added here

if __name__ == "__main__":
    main()
