var gkid;
var table;
var cart_table;
var basket = [];

// Try to increase amount by 1. If not found, return false.
function basket_increase_amount(produkt_id, delta){
    var found = false;
    basket.forEach(function (item)  {
        if (item.productId === produkt_id) {
            found = true;
            if (item.amount < item.stock) item.amount+=delta;
        }
    });
    return found;
}

// Add an item to basket
// If item already exists, just add 1 to amount
function basket_add(produkt_id){
    var found = false;
    if (!basket_increase_amount(produkt_id, 1)){
        var item = {
            productId: produkt_id,
            amount: 1,
            stock: 10,
            customerId: gkid,
        };
        basket.push(item);
        basket_update();
    }
}

// Delete an item from basket
function basket_delete(produkt_id){
    basket = basket.filter(function(value, index, arr) {
        return value.productId !== produkt_id;
    });
    if (basket.length === 0) {basket_hide()}
    basket_update();
}

// Update basket content counter
function basket_update(){
  var element = document.getElementById('basket-num');
  if (basket.length > 0) {
    element.textContent  = "(" + basket.length + ")"; 
  } else {
    element.textContent  = "";
  }
}

// Toggle visibility of cart div
function basket_toggle(){
    $('#basketface').toggleClass('basketface-back')
    $('#basketface').toggleClass('basketface-front')
    cart_table = $('#basket_table').DataTable( {
        destroy: true,
        paging: false,
        autoWidth: true,
        searching: false,
        data: basket,
        columns: [
            { title: "Produkt-id", data: "productId"},
            { title: "Antall",
            orderable:      false,
            data:           null,
            defaultContent: '0', 
            width: "20%",
            render: function ( data, type, row ) 
                { return '<button class="adjust-button" onClick="pb_increase(this, -1)">-</button>' 
                    + '<input id="product-quantity-'
                    + row.productId
                    + '"'
                    + ' pattern="[0-9]*" value="'
                    + row.amount
                    +'" maxlength="3" class="adjust-input" type="text">'
                    + '<button class="adjust-button" onClick="pb_increase(this, 1)">+</button>' ; },
            },
        ]
    })
}

//Send basket to database, and clear it
function basket_send() {
    $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFTOKEN', csrftoken);
        }
    });
    $.ajax({
        type: 'POST',
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        accept: "application/json",
        url: 'http://127.0.0.1:8000/orders/',
        data: JSON.stringify({
            "ordre_dato": new Date(),
            "belop_u_mva": 0,
            "mva_belop": 0,
            "totalbelop": 0,
            "notat": "",
            "kunde": gkid,
            "status": "NY"
        }),
        success: function(msg){
            alert('Success: ' + msg);
        },
        failure: function(msg){
            alert('Failure: ' + msg);
        },
        done: function(msg){
            alert('Done: ' + msg);
        },
    });

    basket=[];
    basket_update();
    basket_toggle();
}

// Called at startup, populate customer data and productlist
function init_kunde(kid) {
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

    //Activate shopping basket for clicking
    document.getElementById('shoppingcart-button').addEventListener('click', function (e) {basket_toggle();});
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
            { visible: false, title: "Opprinnelse", data: "produktopprinnelse"},
            { title: "Årgang", data: "produktaar"},
            { title: "Pris", data: "pris_u_mva"},
            { title: "Lager", data: "beholdning"},
             { orderable:      false,
            data:           null,
            render: function ( data, type, row ) 
                { return '<button class="buy-button" onClick="basket_add('+row.produkt_id+')">Kjøp</button>' ; },
            },

        ],
    } );
};

// Send request
request.send();

// Update amount for the correct row. Make sure amount doesn't exceed stock
// or go below 1.
function pb_increase(context, amount) {
    var data = cart_table.row( $(context).parents('tr') ).data();
    var target = '#product-quantity-'+data.productId;
    var result = parseInt($(target).val())+amount;
    if (result > 0 && result <= data.stock) {
        $(target).val(result);
        basket_increase_amount(data.productId, amount);
    }
}