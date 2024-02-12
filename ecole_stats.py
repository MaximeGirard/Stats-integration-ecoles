import argparse
import pandas as pd
from cpge_data_analysis import extract_data, plot_graph

def main():
    parser = argparse.ArgumentParser(description='Extraire les données et tracer le graphique à partir du fichier CSV CPGE prétraité.')
    
    # Add command-line arguments
    parser.add_argument('csv_file', type=str, nargs='?', default='preprocessed_classement_cpge_2024.csv', help='Chemin vers le fichier CSV CPGE prétraité (par défaut: preprocessed_classement_cpge_2024.csv)')
    parser.add_argument('--ecole', type=str, default="Télécom Paris", help='Nom de l\'école (par défaut: "Télécom Paris")')
    parser.add_argument('--filiere', type=str, help='Filière')
    
    # Add optional arguments for help, list of schools, and list of filieres
    parser.add_argument('--liste-ecoles', action='store_true', help='Lister toutes les écoles disponibles')
    parser.add_argument('--liste-filieres', action='store_true', help='Lister toutes les filières disponibles')
    
    args = parser.parse_args()

    if args.liste_ecoles:
        # Lire le fichier CSV dans un DataFrame pandas
        df = pd.read_csv(args.csv_file)

        # Extraire les écoles uniques
        ecoles_uniques = set()
        for _, row in df.iterrows():
            text = eval(row['Texte'])
            for ecole in text.keys():
                ecoles_uniques.add(ecole)

        print("Liste des écoles disponibles:")
        for ecole in ecoles_uniques:
            print(f"- \"{ecole}\"")
        
    elif args.liste_filieres:
        # Lire le fichier CSV dans un DataFrame pandas
        df = pd.read_csv(args.csv_file)

        # Extraire les filières uniques
        filieres_uniques = df['Filière'].unique()

        print("Liste des filières disponibles:")
        for filiere in filieres_uniques:
            print(f"- \"{filiere}\"")
        
    else:
        # Lire le fichier CSV dans un DataFrame pandas
        df = pd.read_csv(args.csv_file)

        # Extraire les données
        lycée_people_data = extract_data(df, args.ecole, args.filiere)

        # Tracer le graphique
        plot_graph(lycée_people_data, args.ecole, args.filiere)

if __name__ == '__main__':
    main()