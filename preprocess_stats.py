import csv
import requests
from collections import defaultdict

# Define a function to convert the text in the last column to the desired format
def convert_text_to_dict(text):
    data = {}
    lines = text.split("\n")
    for line in lines:
        if line.strip().startswith("-"):
            parts = line.strip().split(":", 1)  # Split on the first occurrence of ':'
            school = parts[0].replace('-', '', 1).strip()
            value = int(parts[1].strip())
            data[school] = value
    return data

# Download the CSV file
url = 'https://www.lefigaro.fr/fig-data/amplifico-infog/BNC6U3n55wCFstVcy9Nk/classement_cpge_2024_amplifico.csv'
response = requests.get(url)
if response.status_code == 200:
    with open('classement_cpge_2024_amplifico.csv', 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download the file. Exiting...")
    exit()

# Read the downloaded CSV file
with open('classement_cpge_2024_amplifico.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Create a list to store modified rows
    modified_rows = []
    
    for row in reader:
        # Modify the last column
        modified_row = dict(row)
        modified_row['Texte'] = convert_text_to_dict(modified_row['Texte'])
        
        modified_rows.append(modified_row)

# Write the modified data back to a new CSV file
with open('preprocessed_classement_cpge_2024.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = modified_rows[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in modified_rows:
        writer.writerow(row)

print("Conversion completed. Output saved to preprocessed_classement_cpge_2024.csv")