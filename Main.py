from Functions import load_data, generate_gender_lists, log_special_character_names, save_data

file_path = 'data/Test Files.xlsx'
df = load_data(file_path)

male_students, female_students = generate_gender_lists(df)

special_names = log_special_character_names(df)

save_data(df)