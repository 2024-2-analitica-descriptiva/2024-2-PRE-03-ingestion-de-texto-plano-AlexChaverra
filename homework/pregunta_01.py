"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    with open("files/input/clusters_report.txt", 'r') as file:
      lines = file.readlines()

    data_lines = lines[4:]

    processed_data = []
    temp_row = []
    current_cluster = True

    for line in data_lines:
        line = line.strip()
        words = line.split()

        if words and current_cluster:
            temp_row = [
                int(words[0]),
                int(words[1]),
                float(words[2].replace(',', '.')),
                " ".join(words[4:]),
            ]
            current_cluster = False

        elif words:
            temp_row[-1] += " " + " ".join(words)
        else:
            
            temp_row[-1] = temp_row[-1].replace('.', '')
            processed_data.append(temp_row)
            temp_row = []
            current_cluster = True

    columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    return pd.DataFrame(processed_data, columns=columns)

print (pregunta_01())