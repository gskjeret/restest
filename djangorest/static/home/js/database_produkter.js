// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/products/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

    $('#produktliste_table').DataTable( {
        data: JSONdata,
        columns: [
                     { title: "id", data: "id"},
                     { title: "Navn", data: "name"},
                     { title: "Pris", data: "price"},
                     { title: "Lager", data: "stock"},
                     { title: "Lev.id", data: "supplier_id"},
        ]
    } );
};


// Send request
request.send();
