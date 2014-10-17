var oTable;
var input;
var viewR;
var addPic;
var name;
var tel;
var direc;
$(document).on('ready',function(){

	/* variables */
	var btnLoad = $('.tblCli');
	var btnCli= $('#btnClientes');
	var btnServicio = $('.btnServicio');
	addPic = $('#btnAddPic'); 
	viewR = $('#lnkRepC');
	$('#tblServicios .tblCli tr').each(function(i,elem){
		//alert($(elem).find(':input').val());
			
	});
	oTable = $('#tblServicios').dataTable({
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
	/* */

	/* ventanas modales */

	$("#myModal").modal({
		show:false,
		backdrop:false,
		keyboard:true
	  });
	$("#modalAltaC").modal({
		show:false,
		backdrop:false,
		keyboard:true
	  });

	$("#ModalRep").modal({
		show:false,
		backdrop:false,
		keyboard:true
	  });

	/* */

	btnCli.on('click',cargarRegistro);
	btnLoad.on('click','tr .btnServicio',addServicio);
	btnLoad.on('click','tr .btnLoad',editCliente);
	viewR.on('click',hisRep);
	addPic.on('click',function(){
		$('#divPicture').slideToggle('slow');
	});
	
});

function addTag(){
	mayor = 0;  
	$('.tblCli tr').each(function(i,elem){
		if($(elem).find(':input').val() > mayor)
			mayor = parseInt($(elem).find(':input').val());
	});
	var template ='<tr> \
					<td><a href="/clientes/detaill_cliente/'+(mayor + 1)+'/">'+$('#frmRegistro .txtNombre').val()+'</a></td> \
					<td>'+$('#frmRegistro .txtDir').val()+'</td> \
					<td>'+$('#frmRegistro .txtTel').val()+'</td> \
					<td>'+$('#frmRegistro .slctCiudad > option:selected').text()+'</td> \
					<td>'+$('#frmRegistro #slctReputacion > option:selected').text()+'</td> \
					<input type="hidden" value="'+(mayor + 1)+'"> \
					<td class="center"><button class="btn btn-primary btn-xs btnLoad"><span class="glyphicon glyphicon-edit"></span></button></td> \
				   </tr>';
	if($('#txtNombre').val() != '' && $('#txtDir').val() != '' && $('#slctCiudad > option:selected').text() != '')			   
		$('.tblCli').prepend($(template).fadeIn('slow'));
}

function addServicio(){
	id=$(this).parent().parent().find(':input').val();
	alert(id);
}

function editCliente ( ) {
	var ruta;
	id=$(this).parent().parent().find(':input').val();
	colnombre = $(this).parent().parent().find('td:eq(0)');
	coldomicilio = $(this).parent().parent().find('td:eq(1)');
	coltelefono = $(this).parent().parent().find('td:eq(2)');
	colciudad = $(this).parent().parent().find('td:eq(3)');
	$("#myModal").modal('show');
	ruta=$('#frmPrueba').attr('action');
	$.ajax({
		type:'get',
		url:'load_cliente',
		data:{'id':id},
		success: function(data){
					$('#frmPrueba').html(data);
					/*$('#frmPrueba').submit(function(e){
						e.preventDefault();
						update();
					});*/
					$('#btnRegistro').on('click',update);
		},
		error:function(xhr,estado,error){
			alert(error);
		},
		timeout:10000
		
	});	
}

function cargarRegistro(){
	$('#modalAltaC').modal('show');
	$.ajax({
			url:'add_cliente',
			success: function(data){
						$('#frmRegistro').html(data);
						$('#slctReputacion option:nth-child(2)').attr('selected','true');
						$('#btnCrear').on('click',registro);
						input = $('#slctPic');
						input.change(function(){
							//alert($(this)[0].files[0].size);
						});
						//$('#frmRegistro').submit(registro);
						/*$("#frmRegistro").submit(function() {
							alert('entro de perdis');
						    var formData = new FormData($(this)[0]);
						    $.post($(this).attr("action"), formData, function(response) {
						       alert(response);
						    });
						    return false;
						});		*/

//
			},
			error:function(xhr,estado,error){
			},
			timeout:10000
	});
}


function hisRep(e){
	e.preventDefault();
	var DCli = parseInt($('#idDCli').val());

	$.ajax({

		type:'GET',
		url:'/clientes/lisrep',
		data:{'id':DCli},
		beforeSend:function(){

		},
		success:function(response){
			$('#hRep').html(response);
			$('#ModalRep').modal('show');

		},
		error:function(xhr,estado,error){
				alert(error+' '+estado);
		},

		complete:function(xhr){
			$('#modalAltaC').modal('hide');
			
		},
		timeout:10000

	});
	
}


function registro(e){
	e.preventDefault();
	rutaR =$('#frmRegistro').attr('action');
	name = $('#txtNombre').val();
	tel = $('#txtTel').val();
	direc = $('#txtDir').val();
	if(validate())
		$.ajax({
			type:'POST',
			url:rutaR,
			//url:'add_cliente',
			data:$('#frmRegistro').serialize(),
			dataType: 'text',
			beforeSend:function(){
				$('#spnSpinnerR').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
			},
			success:function(){
				//$('#spnSpinnerR').html('Cliente agregado con éxito');
				addTag(); // agregamos el elemento agregado al DOM
				//oTable.fnReloadAjax();
			},
			error:function(xhr,estado,error){
					alert(error+' '+estado);
			},

			complete:function(xhr){
				$('#modalAltaC').modal('hide');
				
			},
			timeout:10000

			
		});

	else{
		alert('Olvidate ingresar algunos datos obligatorios');
		$('#txtNombre , #txtTel , #txtDir').on('change',function(){
			$(this).css({
				'background-color':'white',
				'color':'black'

			});

		});
	}
}

function update(){
	rutaU = $('#frmPrueba #ruta').val();
	name = $('#txtNombre').val();
	tel = $('#txtTel').val();
	direc = $('#txtDir').val();
	if(validate()){
			$.ajax({
				type:'post',
				url:rutaU + id +'/',
				data:$('#frmPrueba').serialize(),
				dataType:'text',
				beforeSend:function(){
					$('#spnSpinner').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
				},
				success:function(){
					colnombre.text($('#txtNombre').val());
					coldomicilio.text($('#txtDir').val());
					coltelefono.text($('#txtTel').val());
					colciudad.text($('#slctCiudad > option:selected').text());
					//$('.txtNombre').val('');
					//$('#txtDir').val('');
					//$('#txtTel').val('');
					$('#frmRegistro #btnCrear').disabled = true;
				},
				error:function(xhr,estado,error){
						alert(error);
				},

				complete:function(xhr){
					$("#myModal").modal('hide');
				},
				timeout:10000
			});


	}
	
	else{
		alert('Olvidate ingresar algunos datos obligatorios');
		$('#txtNombre , #txtTel , #txtDir').on('change',function(){
			$(this).css({
				'background-color':'white',
				'color':'black'

			});

		});
	}

}

function initTable () {
	oTable = $('#tblServicios').dataTable({
		"oLanguage":{
			"sLengthMenu":"Mostrar _MENU_ resultados",
			"sSearch":"Búsqueda",
			"sInfo":"Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
			"sZeroRecords": "No hay resultados disponibles"
		},

	  	"bPaginate": true,
	  	"bAutoWidth": true,
	  	"bFilter": true,
	  	"bInfo": false, 
	  	"bJQueryUI": false 

	});
}

function validate(){

	if(name == '' && tel == '' && direc == ''){
		$('#txtNombre').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtTel').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtDir').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtNombre').focus();
		return false;
	}

	if(name == ''){
		$('#txtNombre').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtNombre').focus();
		return false;

	}
	if(tel == ''){
		$('#txtTel').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtTel').focus();
		return false;

	}
	if(direc == ''){
		$('#txtDir').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtDir').focus();
		return false;

	}

	return true;

}