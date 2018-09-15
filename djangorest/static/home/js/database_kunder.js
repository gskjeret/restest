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
            { data: "kunde_id"},
            // Denne vil lage en link til kunder/{kundeid}/
            { title: "Navn", data: "kundenavn", "render": function ( data, type, row ) { return "<a href='kunder/" + row.kunde_id + "'>" + data+"</a>"; },},
            { title: "Kode", data: "adresse"}, 
            { title: "Orgnr", data: "telefonnr"}, 
            { visible: false, data: "kontaktperson"}, 
            { visible: false, data: "telefonnr1"}, 
            { visible: false, data: "kontaktperson2"}, 
            { visible: false, data: "telefonnr2"},
            { title: "Email", data: "emailadresse"},
            { title: "Merknad", data: "merknader"},  
            { title: "Kundetype", data: "kundetype"},  
            { visible: false, data: "reg_dato"},
            { visible: false, data: "reg_bruker"},
            { visible: false, data: "endret_dato"},
            { visible: false, data: "endret_bruker"},
        ]
    } );
};

// Send request
request.send();
