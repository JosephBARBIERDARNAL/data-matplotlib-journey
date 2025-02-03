

<br>

### World

- Load the dataset in matplotlib-journey.com

```python
import geopandas as gpd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/world/world.geojson"
df = gpd.read_file(open_url(url))
```

- Load the dataset oustide (any other environment)

```python
import geopandas as gpd

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/world/world.geojson"
df = gpd.read_file(url)
```
