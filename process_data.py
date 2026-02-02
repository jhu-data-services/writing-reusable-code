import pandas as pd
from datetime import datetime, timezone, timedelta
import time
from zoneinfo import ZoneInfo

experiment_1 = pd.read_table("C:/Users/lmckone1/writing-reusable-code/data/experiment_20250126.txt", 
	header = None, 
	names = ["seconds_since_midnight_utc", "atmospheric_pressure_hpa", "hcl_mixing_ratio_ppbv", "o3_mixing_ratio_ppbv"])
experiment_2 = pd.read_table("C:/Users/lmckone1/writing-reusable-code/data/experiment_20250127.txt", 
	header = None, 
	names = ["seconds_since_midnight_utc", "atmospheric_pressure_hpa", "hcl_mixing_ratio_ppbv", "o3_mixing_ratio_ppbv"])

experiment_1['date'] = '2025-01-26'

experiment_2['date'] = '2025-01-27'

experiment_data = pd.concat([experiment_1, experiment_2])

def utc_seconds_to_est_datetime(date, seconds):
		dt_date = pd.to_datetime(date, format = '%Y-%m-%d')
		dt_datetime = datetime.combine(dt_date, datetime.min.time()) + timedelta(seconds=seconds)
		utc_datetime = pd.to_datetime(dt_datetime, utc = True, format = '%Y-%m-%d %H:%M:%S')
		est_datetime = utc_datetime.astimezone(ZoneInfo('America/New_York'))
		return est_datetime

experiment_data['est_datetime'] = experiment_data.apply(lambda row: utc_seconds_to_est_datetime(row['date'], row['seconds_since_midnight_utc']), axis = 1)

print(experiment_data.head(5))

write_csv(experiment_data, "C:/Users/lmckone1/writing-reusable-code/results/experiment_data.csv")

