## Load the dataset from matplotlib-journey.com

```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/walks/walks.csv"
df = pd.read_csv(open_url(url))
```

## Load the dataset oustide (any other environment)

```python
import pandas as pd

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/walks/walks.csv"
df = pd.read_csv(url)
```