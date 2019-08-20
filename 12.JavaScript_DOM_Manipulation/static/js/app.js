//from data.js store data in a variable 
var tableData = data;

var tbody = d3.select("tbody");
// This function Populates the table by grabbing the <tbody> tag from the HTML file, adding a <tr> tag 
// that adds a row to the table for every Object in the data list. Add <td> tags inside the <tr> tag
// for every key in the Object.  
function populate_table(tableData) {
    tbody.html("");
    // For each dictionary in data that represens a ufo
    tableData.forEach((ufo) => {
        // Add a new row
        var row = tbody.append("tr");
        // For each key and value of the ufo dictionary, insert table data
        Object.entries(ufo).forEach(([key, value]) => {
            row.append("td").text(value);
        })
    });
}


var button = d3.select("#filter-btn");
// When the button is clicked, the value in the input field is stored. The data from data.js file
// is filtered and only the rows that have the value of the datetime key equal to the value of
// the input field are used to populate the table. 
button.on("click", function () {
    d3.event.preventDefault();
    var input_field = d3.select("#datetime");
    var input_date = input_field.property("value");
    if (input_date == "") {
        tableData2 = data;
    } else {
        console.log(input_date);
        filtered_tableData = tableData.filter(ufo => ufo.datetime === input_date);
    }
    populate_table(filtered_tableData);

});
populate_table(tableData);
