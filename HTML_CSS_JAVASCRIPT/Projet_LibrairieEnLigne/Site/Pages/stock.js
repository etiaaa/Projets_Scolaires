$.ajax({
   type: "GET",
   url: "stocks_livres.csv",
   headers: { 
        Accept : "text/csv; charset=utf-8",
        "Content-Type": "text/csv; charset=utf-8"
    },
   dataType: "text",
   success: function(data) {
        var allRows = data.split(/\r?\n|\r/);
	    var table = '<table class="stock_content">';
	    table += '<thead>';
	    table += '<tr>';
		table += '<th>';
		table += 'ID';
		table += '</th>';
	    table += '<th>';
		table += 'LIVRE';
		table += '</th>';
		table += '<th>';
		table += 'CATEGORIE';
		table += '</th>';
		table += '<th>';
		table += 'OPERATION';
		table += '</th>';
		table += '</tr>';
		table += '</thead>';
		table += '<tbody id="myTable_stock">';
	    for (var singleRow = 1; singleRow < allRows.length; singleRow++) {
			var rowCells = allRows[singleRow].split(';');
			var id = rowCells[0];
			var categorie = rowCells[2];
			var livre = rowCells[3];
			table += '<tr class="ligne"><td>'+id+'</td><td>'+livre+'</td><td>'+categorie+'</td><td> <input type="button" id="'+id+'" class="supprimer" value="Supprimer"></td></tr>';
			
		}
		table += '</tbody>';
		table += '</table>';
	    $('.stock').append(table);
   },
   error: function(request, status, error) {
      //alert(request.responseText);
	  //alert(Object.keys(request))
	  //alert(chr.responseText)
	  var errorMessage = request.status + ': ' + request.statusText
      alert('Error - ' + errorMessage);
	  console.log(testStatus)

   }
});

$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable_stock tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
  
  /* action a realiser lorqu'on clique sur le bouton supprimer */
  $(".supprimer").on("click",function(){
	  //var fs = require('fs');
	  //var sample = 'sample.csv';
	  //var id = $(this).attr("id");
	  //suppression du la balise <tr> lorsqu'on clique sur le bouton suppression
	  $(this).parent('td').parent('tr').hide();
	  //$(this).parent('td').parent('tr').remove();
	  //todo
	  // faire un display none pour empecher l'affiche via la recherche
	  
	  
  });

  // Ajout dans le stock
  $("#id_ajouter").on("click",function(){
	  var id = $(this).attr("id");
	 
	  /*
	  $("#tblEntAttributes tbody").append(newRowContent);
	  ------
	  $('#table').append('<tr><td>COL1</td><td>COL2</td></tr>');
	  
	  */
	  var id = $("#id").val();
      var livre = $("#livre").val();
	  var categorie = $("#categorie").val();
	  var chemin = $("#chemin").val();
	  var tr = '<tr><td>'+id+'</td><td>' + livre + '</td><td>' + categorie + '</td><td> <input type="button" id="'+id+'" class="supprimer" value="Supprimer"></td>+</tr>';
	  //ajout de tr dans le tableau
	  $("#myTable_stock").append(tr)
  });

  
});

