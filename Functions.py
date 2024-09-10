import pandas as pd
import re
import logging

logging.basicConfig(filename = 'logs/student_processing.log', level = logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_data (file_path):
    return pd.read_excel(file_path, engine="openpyxl")

def generate_gender_lists(df):
    male_students = df[df['Gender'] == 'M']
    female_students = df[df['Gender'] == 'F']
    logging.info(f"Number of male students: {len(male_students)}")
    logging.info(f"Number of female students: {len(female_students)}")
    return male_students, female_students

def log_special_character_names(df):
    special_names = df[df['Student Name'].str.contains(r'[^a-zA-Z\s]', regex=True)]
    logging.info(f"Names with special characters: {special_names['Student Name'].tolist()}")
    return special_names

def save_data(df):
    df.to_csv('output/students.csv', index=False)
    df.to_csv('output/students.tsv', index=False, sep='\t')
    logging.info("Data saved to CSV and Tsv format.")
