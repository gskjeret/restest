// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/suppliers/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

    $('#leverandorliste_table').DataTable( {
        data: JSONdata,
        columns: [
            { data: "id"},
            { title: "Navn", data: "name"},
            { visible: false, title: "Addresse", data: "address1"},
            { visible: false, title: "", data: "address2"},
            { visible: false, title: "", data: "address3"},
            { visible: false, title: "", data: "postnr"},
            { title: "Poststed", data: "poststed"},
            { title: "Tlf.", data: "phone"},
            { title: "Email", data: "email"},
            { title: "Web", data: "webpage"},
]
    } );
};


// Send request
request.send();
