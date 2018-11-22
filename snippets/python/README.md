# GRID API Snippets
This python code snippet provides convenient access to the GRID API Datasets for Python developers.

# Requirements
- Install requests library: `pip instal requests`
- Access the API documentation here: https://api.grid-nigeria.org/docs

# Sample Usage

```python
from grid_api.py import datasets

resource_name = "schools" # Name of endpoint
size = 10 # Number of items to return
page = 1 # Page Number to return
sort_by = "lga_name" # Field used in sorting responses
fields = "lga_name,state_name,ward_name" # Comma-separated list of fields (No space)
cql = "state_name IN ('Kaduna', 'Kano')" # Read documentations about Querying/Filtering (CQL)

respoonse = datasets(resource_name=resource_name, size=size, cql=cql) # You can optionally pass other parameters as defined above
print(response)
```

* Required Parameters: `resource_name`
* Optional Parameters: `size`, `page`, `sort_by`, `fields`
* Some Values for `sort_by` and `fields` Parameters: *geom,geometry_type,latitude,longitude,global_id,name,ward_code,ward_name,lga_code,lga_name,state_code,state_name*
* Note that the above values for: `sort_by` and `fields` depends on the target `resource_name`

## Querying / Filtering datasets using CQL
The datasets exposed via the GRID API can be queried using the [common query language (CQL)](https://docs.geoserver.org/stable/en/user/tutorials/cql/cql_tutorial.html). 
The CQL is a query language created by the OGC for the Catalogue Web Services specification.
To learn more about how to build CQL expressions checkout [this](https://hicsuntdra.co/blog/geoserver-guide-to-cql/) and [this](http://suite.opengeo.org/docs/latest/geoserver/tutorials/cql/cql_tutorial.html#cql-tutorial)

### CQL Examples
CQL supports following operators:

Comparison operators: `=`, `<>`, `>`, `>=`, `<`, `<=` <br>
Id, list and other operators: `BETWEEN`, `BEFORE`, `AFTER`, `LIKE`, `IS`, `EXISTS`, `NOT`, `IN` <br>
Arithmetic expression operators: `+`, `-`, `*`, `/` <br>
Geometric operators: `EQUALS`, `DISJOINT`, `INTERSECTS`, `TOUCHES`, `CROSSES`, `WITHIN`, `CONTAINS`, `OVERLAPS`, `RELATE`, `DWITHIN`, `BEYOND` <br>

- Scenario:
    Get all datasets from API where `state_name` is `Kano` and `Kaduna`.

    Field name: `state_name`<br>
    Operator: `IN`<br>
    Value: `('Kaduna', 'Kano')`

## Issues
If you find a bug, please file an issue [here](https://github.com/eHealthAfrica/grid-hackathon/issues)