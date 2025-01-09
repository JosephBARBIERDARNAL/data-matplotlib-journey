import pandas as pd
from datasets import all_datasets


def make_full_url(dataset: str):
    return f"https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/{dataset}/{dataset}.csv"


for dataset in all_datasets:
    df = pd.read_csv(make_full_url(dataset))

    print("-" * 50)  # Separator line
    print(f"Dataset: {dataset}")
    print(f"Shape: {df.shape}")
    print("Columns:")
    for i, col in enumerate(df.columns, start=1):
        print(f"  {i}. {col}")
    print("-" * 50 + "\n\n")
