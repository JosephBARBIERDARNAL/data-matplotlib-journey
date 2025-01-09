## Load the dataset from matplotlib-journey.com

```python
import pandas as pd
from pyodide.http import open_url

url = "https://github.com/JosephBARBIERDARNAL/data-matplotlib-journey/blob/main/storms/storms.csv?raw=true"
df = pd.read_csv(open_url(url))
```

## Load the dataset oustide (any other environment)

```python
import pandas as pd

url = "https://github.com/JosephBARBIERDARNAL/data-matplotlib-journey/blob/main/storms/storms.csv?raw=true"
df = pd.read_csv(url)
```
