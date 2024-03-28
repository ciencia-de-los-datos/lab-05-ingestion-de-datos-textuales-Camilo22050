import os
import pandas as pd
data = []

# Ruta de la carpeta train
#train_folder = 'C:\\Users\\pite1\\OneDrive\\Documentos\\GitHub\\lab-05-ingestion-de-datos-textuales-Camilo22050\\data\\train'
train_folder = 'C:\\Users\\pite1\\OneDrive\\Documentos\\GitHub\\lab-05-ingestion-de-datos-textuales-Camilo22050\\data\\test'

# Recorre cada subcarpeta (negative, neutral, positive)
for label in os.listdir(train_folder):
    label_folder = os.path.join(train_folder, label)
    # Recorre cada archivo de texto en la subcarpeta actual
    if os.path.isdir(label_folder):
        # Recorre cada archivo de texto en la subcarpeta actual
        for file_name in os.listdir(label_folder):
            file_path = os.path.join(label_folder, file_name)
            if file_path.endswith('.txt'):
                # Lee el contenido del archivo de texto
                with open(file_path, 'r', encoding='latin-1') as file:
                    phrase = file.read().strip()  # Lee la frase y elimina espacios en blanco
                # Agrega los datos a la lista
                data.append({'phrase': phrase, 'sentiment': label})

# Crea un DataFrame a partir de los datos
df = pd.DataFrame(data)
df = df.dropna()
#df = df.drop_duplicates()
#print(df.sentiment.value_counts())
df.to_csv('test_dataset.csv', index=False)


