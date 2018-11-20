# GRID API Snippets
This javascript code snippet provides convenient access to the GRID API Datasets for Javascript developers.
# Requirements
- Install requests library: `npm install axios`
- Access the API documentation here: https://api.grid-nigeria.org/docs

# Sample Usage

```javascript
const { datasets } = require('./grid_api.js')

let resource_name = "schools" // Name of endpoint
let size = 200 // Number of items to return
let page = 1 // Page Number to return
let sort_by = "lga_name" // Field used in sorting responses
let fields = "lga_name,state_name,ward_name" // Comma-separated list of fields (No space)

datasets("schools") // You can optionally pass other parameters as defined above
```
* Required Parameters: `resource_name`
* Optional Parameters: `size`, `page`, `sort_by`, `fields`
* Values for `sort_by` and `fields` Parameters: *geom,geometry_type,latitude,longitude,global_id,name,ward_code,ward_name,lga_code,lga_name,state_code,state_name*
* Note that the above values for: `sort_by` and `fields` depends on the target `resource_name`

## Issues
If you find a bug, please file an issue [here](https://github.com/eHealthAfrica/grid-hackathon/issues)