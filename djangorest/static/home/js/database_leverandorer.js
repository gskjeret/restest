// Set menu choice
$(document).ready(function()
{
    $('.main_nav li').removeClass("active");
    $('#nav_lev').addClass("active");
});

function format ( d ) {
    console.log(d.leverandor_id)
 
    var extra_info = '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">';
    extra_info +=
    '<tr>'+
        '<td>Besøksadresse:</td>'+
        '<td>'+d.besoksadresse+'</td>'+
    '</tr>';
    extra_info +=
        '<tr>'+
            '<td>Postadresse:</td>'+
            '<td>'+d.postadresse+'</td>'+
        '</tr>';
    var k1 = d.kontaktperson1 + ", tlf. " + d.telefonnr1;
    var k2 = d.kontaktperson2 + ", tlf. " + d.telefonnr2;
    
    if (d.kontaktperson1 || d.telefonnr1) extra_info +=
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
request.open('GET', 'http://127.0.0.1:8000/suppliers/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

  console.log(JSONdata)

  var table = $('#leverandorliste_table').DataTable( {
        data: JSONdata,
        columns: [
            {   "className":      'details-control',
                "orderable":      false,
                "data":           null,
                "defaultContent": '' },
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

    // Add event listener for showing master-details
    $('#leverandorliste_table tbody').on('click', 'td.details-control', function () {
        console.log("Klikk")
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
