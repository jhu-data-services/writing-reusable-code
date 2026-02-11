import pandas as pd
import numpy as np

experiment_data = pd.read_table("C:/Users/lmckone1/writing-reusable-code/data/experiment_20250126.txt", 
	header = None, 
	names = ["seconds_since_midnight_utc", "atmospheric_pressure_hpa", "hcl_mixing_ratio_ppbv", "o3_mixing_ratio_ppbv"])

experiment_data['date'] = '2025-01-26'

experiment_data['atmospheric_pressure_hpa'] = np.round(experiment_data['atmospheric_pressure_hpa'])

print(experiment_data.head(5))

experiment_data.to_csv("C:/Users/lmckone1/writing-reusable-code/results/experiment_data_2025-01-26.csv")

