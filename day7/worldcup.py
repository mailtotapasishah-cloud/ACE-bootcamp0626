import pandas as pd

csv_path = "day7/archive/WorldCups.csv"

df = pd.read_csv(csv_path)

#print("Loaded World Cups dataset:")
#print("- rows:", df.shape[0])
#print("- columns:", df.shape[1])
#print("\nColumns:", df.columns.tolist())
#print("\nFirst 10 rows:")
#print(df.head(10).to_string(index=False))
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.iloc[1])
print(df.iloc[1:4])
print(df.iloc[2:,2])
print(df.loc[1:4, ["Year", "Country", "Winner"]])
print(df.iloc[2:5,[1,2,4,7,9]])
print(df.index)
print(df.set_index("Year", inplace=True))
print(df.reset_index())