from csv import reader
from collections import defaultdict
import time
from pathlib import Path

path_do_txt = "C:/Users/Pichau/Downloads/google-python-exercises/google-python-exercises/basic/1bilhaodelinhas/data/measurements.txt"

def processar_temperaturas(path_do_txt: Path):
    print("iniciando o processamento do arquivo")

    start_time = time.time()

    temperatura_por_station = defaultdict(list)

    with open(path_do_txt, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_station, temperatura = str(row[0]), float(row[1])
            temperatura_por_station[nome_da_station].append(temperatura)

    print("dados carregados. calculando estatisticas...")

    results = {}

    for station, temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)

        print("estatistica calculada. ordenando...")

        sorted_results = dict(sorted(results.items()))

        formatted_results = {station: f"{temps[0]: .1f}/{temps[1]: .1f}/{temps[2]: .1f}" for station, temps in sorted_results.items()}

        end_time = time.time()
        print(f"processamento cocluido em {end_time - start_time: .2f} segundos")

        return formatted_results

if __name__ == "__main__":
    path_do_txt: Path = Path("C:/Users/Pichau/Downloads/google-python-exercises/google-python-exercises/basic/1bilhaodelinhas/data/measurements.txt")
    resultados = processar_temperaturas(path_do_txt)