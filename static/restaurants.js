
function search(){
    d3.event.preventDefault();
    console.log("test");
    province = d3.select("#province").node().value;
    console.log(province);
    var tbody = d3.select("tbody")
    d3.json("/data2", function(datas){
        tbody.html("")
        filtered_data = datas.filter(d => d.province === province)
        console.log(filtered_data)
        // Erase the table
        // Build the table with filtered data
        filtered_data.forEach(function(restaurant){
            // console.log(select_date);
            var row = tbody.append("tr");   
            row.append("td").text(restaurant.city);
            row.append("td").text(restaurant.name);
            row.append("td").text(restaurant.address);
        })
    })
}

d3.select("#form").on("submit", search);
//form.on("submit", search);