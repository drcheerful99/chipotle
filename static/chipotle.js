
function search(){
    d3.event.preventDefault();
    console.log("test");
    state = d3.select("#state").node().value;
    console.log(state);
    d3.json("/data").then(data => {
        filtered_data = data.filter(d => d.state === state)
        console.log(filtered_data)
        // Erase the table
        // Build the table with filtered data
    })
}

d3.select("#state").on("click", search);