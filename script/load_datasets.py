import pandas as pd
from datasets import all_datasets


def make_full_url(dataset: str, isGeopandas: bool):
    file_extension = "geojson" if isGeopandas else "csv"
    return f"https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/{dataset}/{dataset}.{file_extension}"


for dataset in all_datasets:
    isGeopandas = dataset in ["world"]
    url = make_full_url(dataset, isGeopandas=isGeopandas)
    print(url)
    df = pd.read_csv(url)

    print("-" * 50)  # Separator line
    print(f"Dataset: {dataset}")
    print(f"Shape: {df.shape}")
    print("Columns:")
    for i, col in enumerate(df.columns, start=1):
        print(f"  {i}. {col}")
    print("-" * 50 + "\n\n")
