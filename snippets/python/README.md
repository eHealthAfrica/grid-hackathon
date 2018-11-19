# GRID API Snippets
This python code snippet provides convenient access to the GRID API Datasets for Python developers.
# Requirements
- Install requests library: `pip instal requests`
- Access the API documentation here: https://api.grid-nigeria.org/docs

# Usage

```python
from grid_api.py import fetch

resource_name = "schools" # Name of endpoint
size = 200 # Number of items to return
page = 1 # Page Number to return
sort_by = "lga_name" # Field used in sorting responses
fields = "lga_name,state_name,ward_name" # Comma-separated list of fields (No space)

response = fetch(resource_name) # You can optionally pass other parameters as defined above
print(response)
```
* Required Parameters: `resource_name`
* Optional Parameters: `size`, `page`, `sort_by`, `fields`
* Values for `sort_by` and `fields` Parameters: *geom,geometry_type,latitude,longitude,global_id,name,ward_code,ward_name,lga_code,lga_name,state_code,state_name*

## Issues
If you find a bug, please file an issue [here](https://github.com/eHealthAfrica/grid-hackathon/issues)