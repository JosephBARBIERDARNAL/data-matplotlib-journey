from datasets import all_datasets


def dataset_description(dataset: str):
    content = f"""

<br>

### {dataset.title()}

- Load the dataset from matplotlib-journey.com

```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/{dataset}/{dataset}.csv"
df = pd.read_csv(open_url(url))
```

- Load the dataset oustide (any other environment)

```python
import pandas as pd

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/{dataset}/{dataset}.csv"
df = pd.read_csv(url)
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
        dataset_content = dataset_description(dataset)
        readme_content += dataset_content

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)


if __name__ == "__main__":
    generate_readme()
    print("README.md has been generated successfully!")
