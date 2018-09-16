// Set menu choice
$(document).ready(function()
{
    $('.main_nav li').removeClass("active");
    $('#nav_ordre').addClass("active");
});

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:8000/orders/', true);

request.onload = function () {
  // Begin accessing JSON data here
  var JSONdata = JSON.parse(this.response);

  console.log(JSONdata);

    $('#ordreliste_table').DataTable( {
        data: JSONdata,
        columns: [
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
};


// Send request
request.send();
