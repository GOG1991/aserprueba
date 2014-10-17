var btnG;
$(function(){
	$('.lnkEdo').on('click',lista);
	$('.rdoT').on('click',listaT);
	
	$("#modalGar").modal({
		show:false,
		backdrop:false,
		keyboard:true
	  });

});

function initTable () {
	$('#tblServicios').dataTable({
		"aaSorting":[[1,'desc']],
		"oLanguage":{
			"oPaginate":{
				"sFirst":"Inicio",
				"sLast":"Último",
				"sNext":"Siguiente",
				"sPrevious":"Anterior",
			},
			"sLengthMenu":"Mostrar _MENU_ resultados",
			"sSearch":"Búsqueda",
			"sInfo":"Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
			"sZeroRecords": "No hay resultados disponibles"
		},

	  	"bPaginate": true,
	  	"bLengthChange":false,
	  	"bAutoWidth": true,
	  	"bFilter": true,
	  	"bInfo": false, 
	  	"bJQueryUI": false 

	});
}

function lista(e){
	e.preventDefault();
	number = $(this).data('number');
	ball = $(this);
	$.ajax({
		type:'GET',
		url:'/servicios/filtro/',
		data : {'id':number},
		beforeSend:function(){
			$('#listaS').html('<div style="text-align:center;"><i class="fa fa-spinner fa-spin fa-3x " style="color:#377CB9;"></i> <span style="font-weight:bold;color:#377CB9;"> Cargando espere un momento....</span></div>');
		},
		success:function(response){
			//$('.btnFront').text(resp);
			window.setTimeout(function(){
				$('#listaS').slideUp('slow',function(){
					$(this).html(response);	
					btnG = $('.tblServs');
					initTable();
					btnG.on('click','tr .btnGar',revGar);
				}).slideDown('slow');

			},200);

		},

		error:function(xhr,estado,error){
				alert(error+' '+estado +' '+'Consulte a su proveedor de Software');
		},

		complete:function(xhr){
			
		},

		timeout:10000

	});
}

function listaT()
{
	tipo = $(this).val();
	$.ajax({
		type:'GET',
		url:'/servicios/filtroTiposSer/',
		data : {'id':tipo},
		beforeSend:function(){
			$('#listaS').html('<div style="text-align:center;"><i class="fa fa-spinner fa-spin fa-3x " style="color:#377CB9;"></i> <span style="font-weight:bold;color:#377CB9;"> Cargando espere un momento....</span></div>');
		},
		success:function(response){
			//$('.btnFront').text(resp);
			window.setTimeout(function(){
				$('#listaS').slideUp('slow',function(){
					$(this).html(response);	
					initTable();
				}).slideDown('slow');

			},200);

		},

		error:function(xhr,estado,error){
				alert(error+' '+estado +' '+'Consulte a su proveedor de Software');
		},

		complete:function(xhr){
			
		},

		timeout:10000

	});
}

function revGar(e) {
	e.preventDefault();
	n = $(this).data('ids');
	
 	$.ajax({
		type:'GET',
		url:'/servicios/conteog/',
		data:{'id':n},
		dataType:'text',
		beforeSend:function(){

		},
		success:function(datos){
			$('#divGarantias').html(datos);
			$('#modalGar').modal('show');
		},
		error:function(xhr,estado,error){
			alert(error+' '+estado + 'consulte a su proveedor de software');
		},

		complete:function(xhr){
		
		},
		timeout:10000
	});

}