// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();
var JSONdata;
function last_kunde(kid) {
    if (kid > 0) {
        // Open a new connection, using the GET request on the URL endpoint
        request.open('GET', 'http://127.0.0.1:8000/customers/'+kid+'/', true);

        request.onload = function () {
            // Begin accessing JSON data here
            JSONdata = JSON.parse(this.response);
            fill_form();
        };
        request.send();
    } else {
      JSONdata = null;
      fill_form();
    }
}

function fill_form() {
        $("#form").alpaca({
            "data": JSONdata, 
            "schema": {
                "title":"Endre detaljer",
                "description":"Kundedetaljer",
                "type":"object",
                "properties": {
                    "name": {
                        "type":"string",
                        "title":"Navn",
                        "required":true
                    },
                    "address1": {
                        "type":"string",
                        "title":"Addresselinje 1"
                    },
                    "address2": {
                        "type":"string",
                        "title":"Addresselinje 2"
                    },
                    "address3": {
                        "type":"string",
                        "title":"Addresselinje 3"
                    },
                    "postnr": {
                        "type":"integer",
                        "title":"Ranking",
                        "required":true
                    },
                    "poststed": {
                        "type":"string",
                        "title":"Poststed",
                    },

                    "phone": {
                        "type":"string",
                        "title":"Telefonnr",
                    },
                    "email": {
                        "type":"string",
                        "title":"Kontakt email",
                        "required":true
                    },
                    "webaddress": {
                        "type":"string",
                        "title":"Webaddresse",
                    }
                }
            },
            "options": {
                "form":{
                    "attributes":{
                        "action":"http://httpbin.org/post",
                        "method":"post"
                    },
                    "buttons":{
                        "submit":{}
                    }
                },
            },
            "view" : "bootstrap-edit"
        });
    }
