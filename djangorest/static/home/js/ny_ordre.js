
function last_kunde(kid) {
    var gkid = kid;
    if (kid > 0) {
        // Open a new connection, using the GET request on the URL endpoint
        var request = new XMLHttpRequest();
        request.open('GET', 'http://127.0.0.1:8000/customers/' + kid + '/', true);

        request.onload = function () {
            // Begin accessing JSON data here
            var JSONdata = JSON.parse(this.response);
            $('#kundenavn').text(JSONdata.kundenavn);
        };
        request.send();
    } else {
        console.log("Ukjent kundeID "+kid+" - kan ikke opprette ordre")
    }
}
