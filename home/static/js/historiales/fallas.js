$(function(){
//cargamos el primer modal con los datos para seleccionar la falla
	/*$('#txtFalla').on('click',function(){
		var bntF;
		$.ajax({
			url:'/servicios/fallas/',
			success:function(data){
				$('#selectFalla').html(data);
				$('#myModalFalla').modal('show');
				bntF = $('.tblFallas');
				tabla();
				$('.tblFallas').on('click','tr .btnFalla',addServiceFalla);
			},
			error:function(xhr,estado,error){
				console.log(error);
			},
			timeout:10000
		});
	});*/  // agregada
//si se hace click en el boton para agregar una falla
	/*$('#addfalla').on('click', function(){
		$('#myModalFalla').modal('hide');
		$('#modalAltaF').modal('show');
		$.ajax({
			url:'/add_falla/',
			success:function(data){
				$('#frmRegistroF').html(data);
				$('#btnCrearF').on('click', registroFalla);
			},
			error:function(xhr,estado,error){
			},
			timeout:10000
		});
	}); */ // agregado

	/*function registroFalla(){
		$.post('/add_falla/',$('#frmRegistroF').serialize(),cargardata);
		function cargardata(datos){
			$('#modalAltaF').modal('hide');
			addServiceFalla(datos.id)
		}
	}*/  // agregado

	/*function addServiceFalla(idFalla){
		if(parseInt(idFalla)>=0){
		id=idFalla;
	}
	else 
		id=$(this).parent().parent().find(':input').val();
	$('#selectFalla').val(id);
	alert(id);
	$('#myModalFalla').modal('hide');

	}*/ // agregado

	/*function tabla(){
	$('#tblFalla').dataTable({
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
}*/ // agregado

});