// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();
var JSONdata;
var gkid;
function last_kunde(kid) {
    gkid = kid;
    if (kid > 0) {
        // Open a new connection, using the GET request on the URL endpoint
        request.open('GET', 'http://127.0.0.1:8000/customers/'+kid+'/', true);

        request.onload = function () {
            // Begin accessing JSON data here
            JSONdata = JSON.parse(this.response);
            populate_form("Endre kundedetaljer");
        };
        request.send();
    } else {
      JSONdata = null;
      populate_form("Opprett kunde");
    }
}

// PATCH: Change existing row
// POST: Store new row
function submit_form(value) {
var action;
var posturl;

     if (gkid > 0) {
        action = "PATCH";
        posturl = "http://127.0.0.1:8000/customers/"+gkid+"/";
    } else {
        action = "POST";
        posturl = "http://127.0.0.1:8000/customers/";
    };
    // TODO: Use ajax
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open(action, posturl);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    request.onload = function () {
        // TODO: Error checking

    }
    xmlhttp.send(JSON.stringify(value, null, "  "));
    window.location.replace("http://127.0.0.1:8000/kunder");
}

function populate_form(p_title) {
        $("#form").alpaca({
            "data": JSONdata,
            "schema": {
                "title":p_title,
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
                        "title":"Adresselinje 1"
                    },
                    "address2": {
                        "type":"string",
                        "title":"Adresselinje 2"
                    },
                    "address3": {
                        "type":"string",
                        "title":"Adresselinje 3"
                    },
                    "postnr": {
                        "type":"string",
                        "title":"Postnr",
                        "required":true,
                        "minLength": 4,
                        "maxLength": 4,
                        "format": "9999"
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
                        "format":"email",
                        "title":"Kontakt-email",
                        "required":true
                    },
                    "webpage": {
                        "type":"string",
                        "format":"url",
                        "title":"Webadresse",
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
                        "submit":{
                            "title": "Lagre",
                            "click": function(){
                                this.refreshValidationState(true);
                                if (!this.isValid(true)) {
                                    this.focus();
                                    return;
                                }
                                submit_form(this.getValue());
                            }
                        }
                    }
                },
            },
            "view" : "bootstrap-edit"
        });
    }
