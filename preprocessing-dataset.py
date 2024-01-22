import pandas as pd

df = pd.read_csv("wellness_dataset_original.csv")
df = df.drop(columns=['Unnamed: 3']) # 쓸데 없는 열 제거
df = df[~df['챗봇'].isna()] # NaN 있는 행 제거
