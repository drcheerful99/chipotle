
function search(){
    d3.event.preventDefault();
    console.log("test");
    state = d3.select("#state").node().value;
    console.log(state);
    var tbody = d3.select("tbody")
    d3.json("/data", function(data){
        tbody.html("")
        filtered_data = data.filter(d => d.state === state)
        console.log(filtered_data)
        // Erase the table
        // Build the table with filtered data
        filtered_data.forEach(function(chipotle){
            // console.log(select_date);
            var row = tbody.append("tr");   
            row.append("td").text(chipotle.location);
            row.append("td").text(chipotle.address);
        })
    })
}

d3.select("#form").on("submit", search);
//form.on("submit", search);