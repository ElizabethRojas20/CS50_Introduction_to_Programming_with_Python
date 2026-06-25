import csv
from collections import defaultdict

data = []

with open("Hall_results_batch.csv") as file:
    reader = csv.reader(file)
    for x, y, Rs_ohm, Rs_error, rho_ohmcm, rho_error, n, n_error, mu, mu_error, RH_mean, RH_error, RH_difference_percent in reader:
        data.append({
            "x": x, 
            "y": y, 
            "Rs_ohm": Rs_ohm, 
            "Rs_error": Rs_error, 
            "rho_ohmcm": rho_ohmcm, 
            "rho_error": rho_error, 
            "n": n, 
            "n_error": n_error, 
            "mu": mu, 
            "mu_error": mu_error, 
            "RH_mean": RH_mean, 
            "RH_error": RH_error, 
            "RH_difference_percent": RH_difference_percent
            })


coordinates = []

with open("Hall_results_batch.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x = float(row["x"])
        y = float(row["y"])

        coordinates.append((x, y))

means = []

for (x, y), filas in coordinates.items():

    means = {
        "x": x,
        "y": y,
        "Rs_ohm": sum(float(f["Rs_ohm"]) for f in filas) / len(filas),
        "Rs_error": sum(float(f["Rs_error"]) for f in filas) / len(filas),
        "rho_ohmcm": sum(float(f["rho_ohmcm"]) for f in filas) / len(filas),
        "rho_error": sum(float(f["rho_error"]) for f in filas) / len(filas),
        "n": sum(float(f["n"]) for f in filas) / len(filas),
        "n_error": sum(float(f["n_error"]) for f in filas) / len(filas),
        "mu": sum(float(f["mu"]) for f in filas) / len(filas),
        "mu_error": sum(float(f["mu_error"]) for f in filas) / len(filas),
        "RH_mean": sum(float(f["RH_mean"]) for f in filas) / len(filas),
        "RH_error": sum(float(f["RH_error"]) for f in filas) / len(filas),
        "RH_difference_percent": sum(float(f["RH_difference_percent"]) for f in filas) / len(filas)
    }

    means.append(means)

print(means)