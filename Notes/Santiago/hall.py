import csv
from collections import defaultdict

data = []

with open("Hall_results_batch.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({
            "x": row["x"], 
            "y": row["y"], 
            "Rs_ohm": row["Rs_ohm"], 
            "Rs_error": row["Rs_error"], 
            "rho_ohmcm": row["rho_ohmcm"], 
            "rho_error": row["rho_error"], 
            "n": row["n"], 
            "n_error": row["n_error"], 
            "mu": row["mu"], 
            "mu_error": row["mu_error"], 
            "RH_mean": row["RH_mean"], 
            "RH_error": row["RH_error"], 
            "RH_difference_percent": row["RH_difference_percent"]
            })


coordinates = defaultdict(list)

with open("Hall_results_batch.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x = float(row["x"])  # Assuming x is the third column
        y = float(row["y"])  # Assuming y is the fourth column

        coordinates[(x, y)].append(row)

means = []

for (x, y), filas in coordinates.items():

    mean = {
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

    means.append(mean)

with open("Hall_results_batch_mean.csv", "w", newline="") as file:
    fieldnames = ["x", "y", "Rs_ohm", "Rs_error", "rho_ohmcm", "rho_error", "n", "n_error", "mu", "mu_error", "RH_mean", "RH_error", "RH_difference_percent"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(means)