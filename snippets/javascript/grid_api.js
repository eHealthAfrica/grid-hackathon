const axios = require("axios")

let url = "https://api.grid-nigeria.org/"

const datasets = (resource_name, size = 200, page = 1, sort_by = "global_id", fields = "") => {
    const endpoint = `${url}${resource_name}`
    axios.get(endpoint, {
        params: {
            size: size,
            page: page,
            sort_by: sort_by,
            fields: fields
        }
    }).then(response => {
        console.log(response.data)
        return response.data
    })
}

module.exports.datasets = datasets