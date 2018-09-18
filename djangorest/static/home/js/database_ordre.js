// Set menu choice
$(document).ready(function()
{
    $('.main_nav li').removeClass("active");
    $('#nav_ordre').addClass("active");
});

// Function for details
function format ( d ) {
    console.log(d.ordre_id)
    // `d` is the original data object for the row
var linerequest = new XMLHttpRequest();
linerequest.open('GET', 'http://127.0.0.1:8000/orders/', false);
linerequest.send();
var JSONdata = JSON.parse(linerequest.response);
    var linetable = DataTable( {
        
        data:         JSONdata,
        columns: [                   
                     { data: "ordrelinje_id"},
                     { title: "Linjenr", data: "linjenr"},

        ]
    } );
return linetable;
}

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/orders/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

    var table = $('#ordreliste_table').DataTable( {
        
        data: 
        JSONdata,
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
