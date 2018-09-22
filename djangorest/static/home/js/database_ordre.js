// Set menu choice
$(document).ready(function()
{
    $('.main_nav li').removeClass("active");
    $('#nav_ordre').addClass("active");
});

function format ( d ) {
    var extra_info = '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">';
    return "";
}

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/orders/', true);

request.onload = function () {
    // Begin accessing JSON data here
    var JSONdata = JSON.parse(this.response);
    var table = $('#ordreliste_table').DataTable( {
        
        data:    JSONdata,
        columns: [
                    {   "className":      'details-control',
                        "orderable":      false,
                        "data":           null,
                        "defaultContent": '' },
                     { data: "ordre_id"},
                     { title: "KundeID", data: "kunde"},
                     { title: "Best.dato", data: "ordre_dato"},
                     { title: "Status", data: "status"},
                     { title: "Sum u mva", data: "belop_u_mva"},
                     { title: "Mva", data: "mva_belop"},
                     { title: "Totalsum", data: "totalbelop"},
                     { title: "Notat", data: "notat"},
        ]
    } );

    // Add event listener for showing master-details
    $('#ordreliste_table tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row( tr );
        if ( row.node().classList.contains('shown'))  {
            // This row is already shown - unshow it and hide details table
            $('tr').removeClass();
            console.log($('#ordrelinjeliste_table').DataTable)
            $('#ordrelinjeliste_table').DataTable().destroy(false);
            $('#ordrelinjeliste_table').empty();
        } else {
            // Remove shown attribute from all rows
            $('#ordreliste_table tbody tr.shown').removeClass('shown');
            // Add it to just this row
            tr.addClass('shown');
            // Asynchronously display orderlines
            var linerequest = new XMLHttpRequest();
            linerequest.open('GET', 'http://127.0.0.1:8000/v_ordrelinje/?order='+row.data().ordre_id, true);
            linerequest.onload = function () {
                var JSONlinedata = JSON.parse(this.response);
                var linetable = $('#ordrelinjeliste_table').DataTable( {
                    destroy: true,
                    data: JSONlinedata,
                    columns: [
                                { data: "ordrelinje_id"},
                                { data: "ordre"},
                                { title: "Linje", data: "linjenr"},
                                { title: "kode", data: "produktkode"},
                                { title: "Produkt", data: "produktnavn"},
                                { title: "Rabatt%", data: "rabatt_pros"},
                                { title: "Beløp", data: "belop_linje_u_mva"},
                                { title: "Kommentar", data: "kommentar"},
                            ]
                });
            } 
        linerequest.send();
        }
    } 
)} 

// Send request
request.send();
