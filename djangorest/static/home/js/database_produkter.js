// Set menu choice
$(document).ready(function()
{
    $('.main_nav li').removeClass("active");
    $('#nav_produkter').addClass("active");
});

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
             { visible: false, data: "produkt_id"},
             { title: "Produktkode", data: "produktkode"},
             { title: "Navn", data: "produktnavn", "render": function ( data, type, row ) { return "<a href='produkter/" + row.produkt_id + "'>" + data+"</a>"; },},
             { visible: false, title: "Beskrivelse", data: "beskrivelse"},
             { title: "Kategori", data: "produktkategori"},
             { title: "Type", data: "produkttype"},
             { title: "Opprinnelse", data: "produktopprinnelse"},
             { title: "Årgang", data: "produktaar"},
             { title: "Pris", data: "pris_u_mva"},
             { title: "På lager", data: "beholdning"},
             { title: "Leverandør", data: "leverandor"},
             { visible: false, data: "reg_dato"},
             { visible: false, data: "reg_bruker"},
             { visible: false, data: "endret_dato"},
             { visible: false, data: "endret_bruker"},
        ]
    } );
};

// Send request
request.send();
