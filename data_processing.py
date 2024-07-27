import pandas as pd
from config import CSV_FILE_PATH
df = pd.read_csv(CSV_FILE_PATH)

cleaned_df = df.drop_duplicates(subset='user_dim_nk', keep='first')

print("Number of duplicate user_dim_nk:", cleaned_df['user_dim_nk'].duplicated().sum())  # Should be 0

df.to_csv("cleaned.csv")