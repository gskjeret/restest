// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/orders/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

    $('#ordreliste_table').DataTable( {
        data: JSONdata,
        columns: [
                     { data: "id"},
                     { title: "KundeID", data: "customer_id"},
                     { title: "Best.dato", data: "order_date"},
                     { title: "Sendt dato", data: "ship_date"},
                     { title: "Totalsum", data: "total_cost"},
                     { title: "Bet.dato", data: "paid_date"},
        ]
    } );
};


// Send request
request.send();
