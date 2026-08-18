import pandas as pd
import csv


csv_path = r"C:\Users\nikla\Desktop\github_projects\CatBondPricing_EVT\data\earthquakes_us_1950-2026.csv"
out_path = r"CatBondPricing_EVT\data"


raw_data = pd.read_csv(csv_path) 
print(raw_data)
