// Set menu choice
$(document).ready(function()
{
    $('.main_nav li').removeClass("active");
    $('#nav_kunder').addClass("active");
});


function format ( d ) {
    console.log(d.kunde_id)
 
    var extra_info = '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">';
    var k1 = d.kontaktperson + ", tlf. " + d.telefonnr1;
    var k2 = d.kontaktperson2 + ", tlf. " + d.telefonnr2;
    
    if (d.kontaktperson || d.telefonnr1) extra_info +=
        '<tr>'+
        '<td>Kontaktperson:</td>'+
        '<td>'+ k1 +'</td>'+
    '</tr>';
    if (d.kontaktperson2 || d.telefonnr2) extra_info +=
        '<tr>'+
        '<td>Kontaktperson:</td>'+
        '<td>'+ k2 +'</td>'+
    '</tr>';

extra_info += '</table>';
    return extra_info;
    
}

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/customers/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

    var table = $('#kundeliste_table').DataTable( {
        data: JSONdata,
        columns: [
            {   "className":      'details-control',
                "orderable":      false,
                "data":           null,
                "defaultContent": '' },
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

    // Add event listener for showing master-details
    $('#kundeliste_table tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row( tr );
        if ( row.child.isShown() ) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child( format(row.data()) ).show();
            tr.addClass('shown');
        }
    });    
};

// Send request
request.send();
