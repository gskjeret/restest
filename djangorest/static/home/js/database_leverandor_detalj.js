// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();
var JSONdata;
var glid;

function last_leverandor(lid) {
    glid = lid;
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
            "description": "Leverandørdetaljer",
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "title": "Navn",
                    "required": true
                },
                "address1": {
                    "type": "string",
                    "title": "Adresselinje 1"
                },
                "address2": {
                    "type": "string",
                    "title": "Adresselinje 2"
                },
                "address3": {
                    "type": "string",
                    "title": "Adresselinje 3"
                },
                "postnr": {
                    "type": "string",
                    "title": "Postnr",
                    "required": true,
                    "minLength": 4,
                    "maxLength": 4,
                    "format": "9999"
                },
                "poststed": {
                    "type": "string",
                    "title": "Poststed",
                },
                "phone": {
                    "type": "string",
                    "title": "Telefonnr",
                },
                "email": {
                    "type": "string",
                    "format": "email",
                    "title": "Kontakt-email",
                    "required": true
                },
                "webpage": {
                    "type": "string",
                    "format": "url",
                    "title": "Webadresse",
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
