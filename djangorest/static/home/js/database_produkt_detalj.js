// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();
var JSONdata;
var gpid;

function last_produkt(pid) {
    console.log(pid);
    gpid = pid;
    if (pid > 0) {
        // Open a new connection, using the GET request on the URL endpoint
        request.open('GET', 'http://127.0.0.1:8000/products/' + pid + '/', true);

        request.onload = function () {
            // Begin accessing JSON data here
            console.log(this.response);
            JSONdata = JSON.parse(this.response);
            populate_form("Endre produktdetaljer");
        };
        request.send();
    } else {
        JSONdata = null;
        populate_form("Opprett produkt");
    }
}

function submit_form(value) {
    console.log(JSON.stringify(value));
}

function delete_form() {

}


function populate_form(p_title) {
    $("#form").alpaca({
        "data": JSONdata,
        "schema": {
            "title": p_title,
            "description": "Kundedetaljer",
            "type": "object",
            "properties": {
                "produktnavn": {
                    "type": "string",
                    "title": "Navn",
                    "required": true
                },
                "beskrivelse": {
                    "type": "string",
                    "title": "Beskrivelse",
                    "required": true
                },
                "produktkode": {
                    "type": "string",
                    "title": "Kode",
                    "required": true
                },
                "pris_u_mva": {
                    "type": "number",
                    "centsSeparator": ",",
                    "prefix": "kr.",
                    "suffix": "",
                    "thousandsSeparator": ".",
                    "title": "Pris (uten mva)"
                },
                "beholdning": {
                    "type": "integer",
                    "title": "På lager",
                    default: 0
                },
                "leverandor": {
                    "type": "integer",
                    "title": "Leverandør"
                },
            }
        },
        "options": {
            "form": {
                "attributes": {
                    "action": "http://httpbin.org/post",
                    "method": "post"
                },
                "buttons": {
                    "submit": {
                        "title": "Lagre",
                        "click": function () {
                            submit_form(this.getValue());
                        }
                    },
                    "delete": {
                        "title": "Slett",
                        "click": function () {
                            console.log("Delete form");
                            delete_form();
                        }
                    }
                }
            },
        },
        "view": "bootstrap-edit"
    });
}
