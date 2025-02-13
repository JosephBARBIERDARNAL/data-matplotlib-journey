from datasets import all_datasets


def dataset_description(dataset: str, isGeopandas: bool):
    import_code = "import geopandas as gpd" if isGeopandas else "import pandas as pd"
    read_code = "gpd.read_file" if isGeopandas else "pd.read_csv"
    file_extension = "geojson" if isGeopandas else "csv"
    content = f"""

<br>

### {dataset.title()}

- Load the dataset in matplotlib-journey.com

```python
{import_code}
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/{dataset}/{dataset}.{file_extension}"
df = {read_code}(open_url(url))
```

- Load the dataset oustide (any other environment)

```python
{import_code}

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/{dataset}/{dataset}.{file_extension}"
df = {read_code}(url)
```
"""
    return content


def top_of_README():
    content = """
<!-- Automatically generated, do not change by hand. Use script/generate_README.py instead. -->

# Datasets for [matplotlib-journey.com](https://www.matplotlib-journey.com/)
"""
    return content


def generate_readme():
    readme_content = top_of_README()
    for dataset in all_datasets:
        isGeopandas = dataset in ["world", "us-counties", "newyork", "london"]
        dataset_content = dataset_description(dataset, isGeopandas=isGeopandas)
        readme_content += dataset_content

        with open(f"{dataset}/README.md", "w", encoding="utf-8") as f:
            print(f"Writing: {dataset}")
            f.write(dataset_content)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)


if __name__ == "__main__":
    generate_readme()
    print("README.md has been generated successfully!")
