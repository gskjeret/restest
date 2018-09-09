// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/customers/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

    $('#kundeliste_table').DataTable( {
        data: JSONdata,
        columns: [
                     { data: "id"},
                     { data: "name"},
                     { data: "address1"},
                     { data: "address2"},
                     { data: "address3"},
                     { data: "postnr"},
                     { data: "poststed"},
                     { data: "phone"},
                     { data: "email"},
                     { data: "webpage"},
        ]
    } );
};


// Send request
request.send();
