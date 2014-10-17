var Equipos;
var prueba;
var device;
$(function(){
  // #slctEquipo   #txtSelDev
	Steps = $('#frmRegistroSer');
	Steps.on('click','#txtSelDev',function(){
	//$('#slctEquipo').on('click',function(){
		var btn;
		prueba = $(this);
		$.ajax({
			url:'/servicios/equipos/',
			success:function(data){
				
				$('#selectEqui').html(data);
				$('#myModalEquipo').modal('show');
				btn = $('.tblEquipo');
				//tabla();
				$('.tblEquipo').on('click','tr .btnSerEquipo', addServiceEquipo);
				//$.getScript('/static/servicios/servicios.js',function(){

				//});
				
			},
			error:function(xhr,estado,error){
				console.log(error);
			},
			timeout:10000
		});
		
	});

	$('#addequipo').on('click',function(){
		
		$('#myModalEquipo').modal('hide');
		$('#modalAltaE').modal('show');
		$.ajax({
			url:'/add_equipo/',
			success:function(data){

				$('#frmRegistroE').html(data);
				$('#btnCrearE').on('click',registroEquipo);
				
			},
			error:function(xhr,estado,error){
			},
			timeout:10000

		});
		
	});

	function addServiceEquipo(idEquipo){
			if(parseInt(idEquipo)>=0){
				id=idEquipo;
			}
			else {
				id=$(this).parent().parent().find(':input').val();
				cat = $(this).parent().parent().find(':nth-child(4)').text();
				alert(cat);
				device = id;
			}
			prueba.val(id);
			$('#myModalEquipo').modal('hide');
		}

	function datosJson(datos){
		$('#modalAltaE').modal('hide');
		if(datos.categoria === 'laptop')
		addServiceEquipo(datos.id);
	}		

	function registroEquipo(){
			/*$.ajax({
			type:'POST',
			url:'/add_equipo/',
			//url:'add_cliente',
			data:$('#frmRegistroE').serialize(),
			dataType: 'text',
			beforeSend:function(){
				$('#spnSpinnerR').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
			},
			success:function(data){
				addServiceEquipo(data);
				alert (data['id']);
			},
			error:function(xhr,estado,error){
					alert(error+' '+estado);
			},

			complete:function(xhr){
				$('#modalAltaE').modal('hide');
				
			},
			timeout:10000
=======
function registroEquipo(){
$.post('/add_equipo/',$('#frmRegistroE').serialize(),cargardata);

function cargardata(datos){
	$('#modalAltaE').modal('hide');
	addServiceEquipo(datos.id)
}
>>>>>>> 11c3af4801ab73131f7fe874cdeab248ba53a79f

			
		});
	*/
		 	$.post('/add_equipo/',$('#frmRegistroE').serialize(),datosJson);
		
		}


});