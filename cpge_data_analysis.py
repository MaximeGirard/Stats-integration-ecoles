# cpge_data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def extract_data(df, school_name, filiere):
    # Filter rows based on the filiere
    filtered_df = df[df['Filière'] == filiere]

    # Extract data for the specified school
    school_data = filtered_df[filtered_df['Texte'].str.contains(school_name)]

    # Extract the lycée and the number of people
    lycée_people_data = []
    for _, row in school_data.iterrows():
        lycée = row['Etablissement']
        text = eval(row['Texte'])
        if school_name in text:
            lycée_people_data.append((lycée, text[school_name]))

    return lycée_people_data

def plot_graph(lycée_people_data, school_name, filiere):
    # Sort the data in descending order by the number of intégrés
    lycée_people_data.sort(key=lambda x: x[1], reverse=True)
    
    lycée_names = [data[0] for data in lycée_people_data]
    number_of_people = [data[1] for data in lycée_people_data]

    plt.figure(figsize=(10, 6))
    plt.bar(lycée_names, number_of_people, color='skyblue')
    plt.xlabel('Lycée')
    plt.ylabel('Nombre d\'intégrés')
    plt.title(f'Nombre d\'intégrés par lycée pour {school_name} en {filiere}')
    plt.xticks(rotation=45, ha='right')
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: int(x)))  # Format y-axis ticks as integers
    plt.tight_layout()
    plt.show()