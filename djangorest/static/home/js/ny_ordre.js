var gkid;
var table;

function last_kunde(kid) {
    gkid = kid;
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

var request = new XMLHttpRequest();
request.open('GET', 'http://127.0.0.1:8000/products/', true);
request.onload = function () {
  var JSONdata = JSON.parse(this.response);
  JSONdata["antall"] = 0;
  table = $('#produktliste_table').DataTable( {
        initComplete: function () {
            this.api().columns().every( function (inx) {
                var column = this;
                if (inx>=2 && inx < 6) {
                    var select = $('<select><option value=""></option></select>')
                        .appendTo( $(column.header()) )
                        .on( 'change', function () {
                            var val = $.fn.dataTable.util.escapeRegex(
                                $(this).val()
                            );
    
                            column
                                .search( val ? '^'+val+'$' : '', true, false )
                                .draw();
                        } );
 
                    column.data().unique().sort().each( function ( d, j ) {
                        select.append( '<option value="'+d+'">'+d+'</option>' )
                    } );
                } 
            } );
        },
        data: JSONdata,
        columns: [
            { visible: false, data: "produkt_id"},
            { title: "Navn", data: "produktnavn", render: function ( data, type, row ) { return "<a href='produkter/" + row.produkt_id + "'>" + data+"</a>"; },},
            { title: "Kategori", data: "produktkategori"},
            { title: "Type", data: "produkttype"},
            { title: "Opprinnelse", data: "produktopprinnelse"},
            { title: "Årgang", data: "produktaar"},
            { title: "Pris", data: "pris_u_mva"},
            { title: "Lager", data: "beholdning"},
            { title: "Bestill",
            orderable:      false,
            data:           null,
            defaultContent: '0', 
            width: "15%",
            render: function ( data, type, row ) 
                { return '<button class="adjust-button" onClick="pb_increase(this, -1)">-</button>' 
                    + '<input id="product-quantity-'
                    + row.produkt_id
                    + '"'
                    + ' pattern="[0-9]*" value="1" maxlength="3" class="adjust-input" input-type="number">'
                    + '<button class="adjust-button" onClick="pb_increase(this, 1)">+</button>' ; },
            },
        ],
    } );
};

// Send request
request.send();

function pb_increase(context, amount) {
    var data = table.row( $(context).parents('tr') ).data();
    var target = '#product-quantity-'+data.produkt_id;
    $(target).val(parseInt($(target).val())+amount);
}