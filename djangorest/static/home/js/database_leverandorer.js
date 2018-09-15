// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/suppliers/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

  console.log(JSONdata)

    $('#leverandorliste_table').DataTable( {
        data: JSONdata,
        columns: [
            { data: "leverandor_id"},
            // Denne vil lage en link til leverandorer/{leverandor_id}/
            { title: "Navn", data: "leverandornavn", "render": function ( data, type, row ) { return "<a href='leverandorer/" + row.leverandor_id + "'>" + data+"</a>"; },},
            { title: "Kode", data: "leverandorkode"}, 
            { title: "Orgnr", data: "organisasjonsnr"}, 
            { visible: false, data: "besoksadresse"}, 
            { visible: false, data: "postadresse"}, 
            { visible: false, data: "kontaktperson1"}, 
            { visible: false, data: "telefonnr1"},
            { visible: false, data: "kontaktperson2"},
            { visible: false, data: "telefonnr2"},
            { title: "Email", data: "emailadresse"},
            { title: "Webside", data: "hjemmeside"},
            { title: "Merknad", data: "merknader"},  
            { visible: false, data: "reg_dato"},
            { visible: false, data: "reg_bruker"},
            { visible: false, data: "endret_dato"},
            { visible: false, data: "endret_bruker"},
]
    } );
};


// Send request
request.send();
