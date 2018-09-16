// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();
var JSONdata;
var glid;

function last_leverandor(lid) {
    glid = lid;
    console.log(lid);
    if (lid > 0) {
        // Open a new connection, using the GET request on the URL endpoint
        request.open('GET', 'http://127.0.0.1:8000/suppliers/' + lid + '/', true);

        request.onload = function () {
            // Begin accessing JSON data here
            console.log(this.response);
            JSONdata = JSON.parse(this.response);
            populate_form("Endre leverandørdetaljer");
        };
        request.send();
    } else {
        JSONdata = null;
        populate_form("Opprett leverandør");
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
                "leverandornavn": {
                    "type": "string",
                    "title": "Navn",
                    "required": true
                },
                "leverandorkode": {
                    "type": "string",
                    "title": "Leverandørkode",
                    "enum": ["A", "B", "C", "D", "E", "F"],
                },
                "organisasjonsnr": {
                    "type": "string",
                    "title": "Organisasjonsnummer"
                },
                "besoksadresse": {
                    "type": "string",
                    "title": "Besøksadresse"
                },
                "postadresse": {
                    "type": "string",
                    "title": "Postadresse"
                },
                "kontaktperson1": {
                    "type": "string",
                    "title": "Kontaktperson"
                },
                "telefonnr1": {
                    "type": "string",
                    "title": "Telefonnr"
                },
                "kontaktperson2": {
                    "type": "string",
                    "title": "Kontaktperson (sekundær)"
                },
                "telefonnr2": {
                    "type": "string",
                    "title": "Telefonnr (sekundært)"
                },
                "emailadresse": {
                    "type": "string",
                    "format": "email",
                    "title": "Kontakt-email",
                    "required": true
                },
                "hjemmeside": {
                    "type": "string",
                    "format": "url",
                    "title": "Webadresse",
                },
                "merknader": {
                    "type": "string",
                    "format": "string",
                    "title": "Merknader",
                }
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
                            this.refreshValidationState(true);
                            if (!this.isValid(true)) {
                                this.focus();
                                return;
                            }
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
