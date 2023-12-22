import pandas as pd
import numpy as np
import io

# Funkcja do usuwania danych z kolumny "MINUTES_REMAINING" oraz "SECONDS_REMAINING"
def random_nan_inserter(data, column_name, num_of_nans):
    num_of_nans = min(num_of_nans, len(data))
    nan_indices = np.random.choice(data.index, size=num_of_nans, replace=False)
    data.loc[nan_indices, column_name] = np.nan
    return data

# Wczytanie danych
file_path = r'C:\Users\Artur_S\Desktop\2000-2023.csv'  # Zmień na ścieżkę do twojego pliku
data = pd.read_csv(file_path)

# Ręczne usuwanie niektórych wartości z kolumny "MINUTES_REMAINING" oraz SECONDS_REMAINING
data = random_nan_inserter(data, 'MINUTES_REMAINING', 10)
data = random_nan_inserter(data, 'SECONDS_REMAINING', 10)

head_md = data.head().to_markdown()
nulls_md = data.isnull().sum().to_frame().to_markdown()
buffer = io.StringIO()
data.info(buf=buffer)
info_md = buffer.getvalue()

# Zapisywanie opisu danych i informacji o braku danych do pliku Markdown
with open('data_description.md', 'w', encoding='utf-8') as file:
    file.write("# Opis Danych\n\n")
    file.write("## Pierwsze 5 wierszy danych\n")
    file.write(head_md + "\n\n")
    file.write("## Informacje o danych\n")
    file.write("```\n" + info_md + "```\n")
    file.write("## Informacja o braku danych (liczba brakujących wartości)\n")
    file.write(nulls_md + "\n")


# zapiswyanie danych do pliku CSV i Excel jako malą próbkę
data.to_csv('data_output.csv', index=False)
sampled_data = data.sample(frac=0.002)
sampled_data.to_excel('data_output.xlsx', index=False, engine='openpyxl')
