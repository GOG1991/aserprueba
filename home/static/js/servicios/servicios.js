var Steps;
var addEquipo;
var nombre;
var device;
var contraseña;
var respaldo;
var cat;
var idc;
var equipos;
var btnLoad;
var falla;
var tipoSer;
var acategorias = new Array();
var devices =  new Array();
var fallas = new Array();
var selRad = new Array();
var bntAcceE;
var btnAcceBd;
var enRes;
var fol;
var name;
var tel;
var direc;
var nameF;
var descF;
var modEq;
var descEq;
var devSel;
$(function(){

	fol = $('#nserieAl').val();
	if($('#txtSelCli').val() == '')
		$('#btnStep1').attr('disabled','true');		
	else
		$('#btnStep1').removeAttr('disabled');





	//$('#formSet').formset({
	//	prefix:'{{ detalleFormset.prefix }}'
	//});	
	/* $('#tableForm tbody tr').formset({
                   prefix: '{{ servicios detalle }}',
           
               });*/
	
	/*enRes='<span>Pedir Contraseña</span> \
		 <label class="radio-inline"> \
				<input type="radio" name="inlineRadioOptions" id="radio1" class="rdoC" value="1"> si \
			 </label> \
			  <label class="radio-inline"> \
		  <input type="radio" name="inlineRadioOptions" id="radio2"  class="rdoC" value="2"> no \
			 </label>'; radios para pedir contraseña */

	bntAcceE = $('#btnEAcc');
	btnAcceBd=$('#btnEwAcc');
	var divStep = $('#btnStep');
	var txtCliente = $('#txtSelCli');
	addEquipo = $('#addEquipo');
	addEquipo.attr('disabled','true');
	Steps = $('#frmRegistroSer');
	//$('#btnStep1').attr('disabled','true');
	divStep.html("<span class='spnStep' id='btnStep'>paso 1 de 2</span>");

	// ventana modal para agregar y buscar clientes
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
		$("#myModalEquipo").modal({
		show:false,
		backdrop:false,
		keyboard:true
	  });

	 $('#modalAltaE').modal({
	 	show:false,
	 	backdrop:false,
	 	keyboard:true
	 });
	 $('#myModalEquipo').modal({
	 	show:false,
	 	backdrop:false,
	 	keyboard:true
	 });

	 $('#modalEqAcce').modal({
	 	show:false,
	 	backdrop:false,
	 	keyboard:true
	 });
	/*$('#txtCliente').on('change',function(){
		//$('#btnStep1').removeAttr('disabled');
		$('#btnStep1').fadeIn('slow');
	});*/
	 
	/*$('#btnStep1').attr('disabled','true');
	divStep.html("<span class='spnStep' id='btnStep'>paso 1 de 3</span>");

	$('#slctCli').on('change',function(){
		$('#btnStep1').removeAttr('disabled');
	});
	*/
	
    // personalizacion datapicker a español
	//var date=new Date();
	//$( "#txtFecha" ).datetimepicker({showAnim: 'clip',setDate:new Date(),dateFormat:'dd/mm/yy'});
	//$('#txtFecha').val(date.getDate()+'-'+(date.getMonth()+1)+'-'+date.getFullYear());
	
	$('#slctProducto').on('change',function(){
		$('#txtFechaProducto').removeAttr('disabled');
	});
	//$('#slctTipoSer').on('change',function(){
	Steps.on('change','#slctTipoSer',function(){
		if($(this).val() == 2){
			$('#txtDireccion').removeAttr('disabled');
			$('#fechaInicio,#fechaFin').removeAttr('disabled');
			tipoSer = parseInt($(this).val());
			fechaHoras();
		}
		else{

			$('#txtDireccion').attr('disabled','true');
			$('#fechaInicio,#fechaFin').attr('disabled','true');
			tipoSer = parseInt($(this).val());
		}
	});
    // campos desabilitados para servicio local

	
    // opciones de datatimepicker para desabilitar dias y horas
    Steps.on('click','#btnStep1,#btnStep2',Slides);
    Steps.on('click','#btnStep3,#btnStep4',Slidesp3); //para que fueran 2 pasos
	//$('#btnStep1,#btnStep2').on('click',Slides);
	//$('#btnStep3,#btnStep4').on('click',Slidesp3);
	$('#slctTipoSer option:nth-child(2)').attr('selected','true');
	$('#slctEstado option:nth-child(2)').attr('selected','true');
	$('#slctTecnico option:nth-child(2)').attr('selected','true');
	$('#slctTipoMant option:nth-child(2)').attr('selected','true');

	
	// funciones llamadas al selecconar fecha de finalizacion de un servicio

	function Slides(e){
		e.preventDefault();
		if($(this).attr('id') == 'btnStep1')
			divStep.slideUp('slow',function(){
				$(this).html("<span class='spnStep' id='btnStep'>paso 2 de 3</span>");		
			}).slideDown('slow');
		else
			divStep.slideUp('slow',function(){
				$(this).html("<span class='spnStep' id='btnStep'>paso 1 de 3</span>");
			}).slideDown('slow');
			
		$('.divP1').slideToggle("slow");
		$('.divP2').slideToggle("slow");
	}

	function Slidesp3(e){
		e.preventDefault();
		if($(this).attr('id') == 'btnStep3'){
			devSel = document.getElementsByClassName('txtSelEquipo');
			var ban = 0;
			for(var i=0, l=devSel.length; i<= l-1; i++){
				if(devSel[i].value == ''){
					ban ++;
					devSel[i].style.background = 'red';
					if(ban == 1)
						devSel[i].focus();
				}else
					devSel[i].style.background = 'white';
				
			}
			if(ban > 0)
				alert('Debes seleccionar un equipo para poder agregarlo al servicio revisa los campos de color rojo');
			else{
				divStep.slideUp('slow',function(){
					$(this).html("<span class='spnStep' id='btnStep'>paso 3 de 3</span>");					
				}).slideDown('slow');
				$('.divP2').slideToggle("slow");
				$('.divP3').slideToggle("slow");
			}
		
		}	
		else{
			divStep.slideUp('slow',function(){
				$(this).html("<span class='spnStep' id='btnStep'>paso 2 de 3</span>");
			}).slideDown('slow');

			$('.divP2').slideToggle("slow");
			$('.divP3').slideToggle("slow");
		}
						
		//$('.divP2').slideToggle("slow");
		//$('.divP3').slideToggle("slow");
	}
	// slides en cada paso del registro de un servicio

	$('#addequipo').on('click',function(){ // funcion equipos
		
		$('#myModalEquipo').modal('hide');
		$.ajax({
			url:'/add_equipo/',
			success:function(data){	
				nserie = Math.floor(Math.random()*1000008);
				$('#divEquipo').html(data);
				$('#id_noserie').val(fol+'&'+nserie);
				$('#modalAltaE').modal('show');
				$('#slctAcce option:nth-child(1)').attr('selected','true');
				//$('#modalAltaE').modal('hide');
				$('#btnCrearE').on('click',registroEquipo);
				
			},
			error:function(xhr,estado,error){
			},
			timeout:10000

		});
		
	});

	$('#botonP').on('click',function(){
		$('#myModal').modal('hide');
		$.ajax({
			url:'/clientes/add_cliente/',
			success:function(data){
				$('#frmRegistro').html(data);
				$('#modalAltaC').modal('show');
				$('#slctReputacion option:nth-child(2)').attr('selected','true');
				$('#btnCrear').on('click',registro);
			},
			error:function(xhr,estado,error){
			},
			timeout:10000

		});

		/*$.ajax({
			url:'/clientes/add_cliente/',
			success: function(data){
						$('#selectCli').html(data);
						$('#slctReputacion option:nth-child(2)').attr('selected','true');
						$('#btnCrear').on('click',registro);




			},
			error:function(xhr,estado,error){
			},
			timeout:10000
		});*/
	});

	$('#addfalla').on('click', function(){
			$('#myModalFalla').modal('hide');
			$.ajax({
				url:'/add_falla/',
				success:function(data){
					$('#frmRegistroF').html(data);
					$('#slctCatF option:nth-child(1)').attr('selected','true');
					$('#modalAltaF').modal('show');
					$('#btnCrearF').on('click', registroFalla);
				},
				error:function(xhr,estado,error){
				},
				timeout:10000
			});
		});

	// ajax 
	Steps.on('click','#txtFalla',function(){   // fallas
	//$('#txtFalla').on('click',function(){
		var bntF;
		tempFalla = $(this);
		$.ajax({
			url:'/servicios/fallas/',
			success:function(data){
				$('#selectFalla').html(data);
				$('#myModalFalla').modal('show');
				bntF = $('.tblFallas');
				initTable('#tblFalla');
				$('.tblFallas').on('click','tr .btnFalla',addServiceFalla);
			},
			error:function(xhr,estado,error){
				console.log(error);
			},
			timeout:10000
		});
	});

	Steps.on('click','#slctEquipo',function(){ // funciones equipos
	//$('#slctEquipo').on('click',function(){
		var btn;
		if(parseInt($('#txtCliente').val()) > 0)
			 idc = parseInt($('#txtCliente').val());
		else
			 idc = 0;
		tempEq = $(this);
		$.ajax({
			// before url:'/servicios/equipos/',
			url:'/filtroE/',
			data:{'id':idc},
			success:function(data){
				
				$('#selectEqui').html(data);
				$('#myModalEquipo').modal('show');
				initTable('#tblEqui');
				btn = $('.tblEquipo');
				$('.tblEquipo').on('click','tr .btnSerEquipo', addServiceEquipo);
				$('.tblEquipo').on('click','tr .btnEAcc', accesorios);
				//$.getScript('/static/servicios/servicios.js',function(){

				//});
				
			},
			error:function(xhr,estado,error){
				console.log(error);
			},
			timeout:10000
		});
		
	});


	Steps.on('click','#addEquipo',function(e){
		e.preventDefault();
		$.ajax({
			url:'/servicios/add_serviceajax/',
			type:'POST',
			data:$('#frmRegistroSer').serialize(),
			dataType: 'text',
			success:function(data){
				$('#frmRegistroSer').html(data);
				$('#txtSelCli').val(nombre);
				// validamos si el servicio es a domicilio para habilitar datos
				validaTipo();
				fechaHoras();
				// agregamos los datos del equipo cuando se agregan más
				equipos = document.getElementsByClassName('txtSelDev');
				// para la opcion de pedir contraseña radios = document.getElementsByClassName('divRespaldo');
				for(var i=0, l=equipos.length; i<l-1; i++){
					equipos[i].innerHTML = devices[i];
					// para pedir contraseña radios[i].innerHTML = enRes;
					//if(selRad[i] == 1)
					//	$('.txtContraseña').removeAttr('disabled');
				}	
				
				// agregamos los datos de la falla cuando se agregan más
				falla = document.getElementsByClassName('spanFalla');
				for(var i=0, l=falla.length; i<l-1; i++){
					falla[i].innerHTML = fallas[i];
				}	

				contraseña = document.getElementsByClassName('txtContraseña');
				respaldo = document.getElementsByClassName('chkRes');
				for(var i=0, l=contraseña.length; i<l-1; i++){
					// aqui en el if iba acategorias[i] if(acategorias[i] == 1 || acategorias[i] == 2)
					if(selRad[i] == 1){
						contraseña[i].disabled = false;
						//respaldo[i].disabled = false;
					}
					else
					{
						contraseña[i].disabled = true;
						//respaldo[i].disabled = true;
					}

				}
	
			},

		});
		/*$(this).css({
			'box-shadow':"0 0 rgba(255,255,255,0.9)inset",
			'font-size':'17px'

		});*/
		
		

		
		
		//for (i in devices)
		//	alert(devices[i]);

		//$('#frmRegistroSer #slctEquipo').each(function(index,elemento){
		//	alert($.data(elemento,'posicio'));
		//});

	});

	Steps.on('click ','#txtSelCli',function(){
		$.ajax({
			url:'/servicios/clientes/',
			success:function(data){
				$('#selectCli').html(data);
				$('#myModal').modal('show');
				initTable('#tblCli');	
			},
			error:function(xhr,estado,error){
				console.log(error);
			},
			timeout:10000
		});
	});
	// ajax
});
//

function acceBd(e){
	e.preventDefault();
	$('#txtidEa').val(id);
	$('#spnAEBD').html('');
	$.ajax({
		type:'POST',
		url:'/updateacc/',
		data:$('#frmAcceBd').serialize(),
		beforeSend:function(){
			$('#spnAEBD').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		},
		success:function(data){
			$('#spnAEBD').html('Registro exitoso');
			$('#modalEqAcce').modal('hide');
		},
		error:function(xhr,estado,error){
			console.log(error);
		},
		complete:function(){
			$('#modalEqAcce').modal('hide');
			$('#spnAEBD').html('');
		},
		timeout:10000

	});

}

function accesorios(e){
	e.preventDefault();
	id=$(this).parent().parent().find('.txtIdEquipo:input').val();

	$.ajax({
		type:'GET',
		url:'/updateacc/',
		data:{'id':id},
		beforeSend:function(){
			$('#spnAcceE').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
			$('#modalEqAcce').modal('show');
		},
		success:function(data){
			$('#equipowacc').html(data);
			$('#spnAcceE').html('');
			btnAcceBd.on('click',acceBd);
		},
		error:function(xhr,estado,error){
			console.log(error);
		},
		complete:function(){
			$('#spnAcceE').html('');
		},
		timeout:10000

	});
}

function addServicio(idCli){
	if($(this).attr('id') == 'btnServicio')
	{
		id = $(this).parent().parent().find(':input').val();
		nombre = $(this).parent().find(':nth-child(1)').text();
	}	
	/*if(parseInt(idCli)>=0){
		id=idCli;
	}*/
	//else id=$(this).parent().parent().find(':input').val();
	else{
		id = idCli.id;
		nombre = idCli.nombre;
		//alert(idCli.nombre+' '+idCli.id);
	}
	$('#txtCliente').val(id);
	$('#txtSelCli').val(nombre);
	$('#myModal').modal('hide');
	$('#modalAltaC').modal('hide');
	$('#btnStep1').removeAttr('disabled');
	$('#spnSpinnerR').html('');
	addEquipo.removeAttr('disabled');
	//$('#btnStep1').fadeIn('slow');
}

function addServiceEquipo(datos){
	var ban = 0;
	devSel = document.getElementsByClassName('txtSelEquipo');
	//alert('entro a addServiceEquipos');
	if($(this).attr('class') == 'btnSerEquipo'){

		id=$(this).parent().parent().find('.txtIdEquipo:input').val();
		cat = parseInt($(this).parent().parent().find('.txtIdCat:input').val());
		device = $(this).parent().parent().find(':nth-child(4)').text()+' '+
			$(this).parent().parent().find(':nth-child(3)').text()+' '+
			$(this).parent().parent().find(':nth-child(2)').text()+' '+
			'número de serie'+' '+$(this).parent().find(':nth-child(1)').text();

	}
	else 
	{
		id = datos.id;
		cat = parseInt(datos.categoriapk);
		device = datos.categoria +' '+datos.modelo+' '+'número de serie'+' '+datos.noserie;
		//idcategoria = datos.categoriapk;
	}
	//$('.divRespaldo').slideDown();
	//$('.rdoC').on('click',enablePass);
	// para que no se repitan
	for(var i=0, l=devSel.length; i<= l-1; i++){
		if(devSel[i].value == id){
			ban ++;
			devSel[i].focus();
		}
		
	}
	if(ban > 0)
		alert('No pudes agregar el mismo equipo '+id+' más de una vez al servicio')
	// para que no se repitan
	else{
		tempEq.val(id);
		tempId = document.getElementsByClassName('txtSelDev').length-1;
		contraseña = document.getElementsByClassName('txtContraseña');
		// respaldo = document.getElementsByClassName('chkRes');
		document.getElementsByClassName('txtSelDev')[tempId].innerHTML = device;
		devices.push(device);
		acategorias.push(cat);
	}
	//tempEq.val(id);
	//tempId = document.getElementsByClassName('txtSelDev').length-1;
	//contraseña = document.getElementsByClassName('txtContraseña');
	// respaldo = document.getElementsByClassName('chkRes');
	//document.getElementsByClassName('txtSelDev')[tempId].innerHTML = device;
	// para los radio de pedir contraseña document.getElementsByClassName('divRespaldo')[tempId].innerHTML = enRes;
	// $('.rdoC').on('click',enablePass);
	/*if(cat == 1 || cat == 2)
	{
		contraseña[tempId].disabled = false;
		respaldo[tempId].disabled = false;
	}	
		
	else{
		contraseña[tempId].disabled = true;
		respaldo[tempId].disabled = true;
	}  con esto habilitaba la contraseña segun la categoria*/

	$('#myModalEquipo').modal('hide');
	$('#modalAltaE').modal('hide');
	//devices.push(device);
	//acategorias.push(cat);
}

function addServiceFalla(datos){ // fallas  btnFalla
	cadenaF = '-falla: '
	if($(this).attr('id') == 'btnFalla'){
		id=$(this).parent().parent().find(':input').val();
		falla = cadenaF +' '+$(this).parent().parent().find(':nth-child(1)').text();
	}

	else {
		id = datos.id;
		falla = cadenaF +' '+datos.nombre;
	}

	tempFalla.val(id);
	tempIdFalla = document.getElementsByClassName('spanFalla').length-1;
	document.getElementsByClassName('spanFalla')[tempIdFalla].innerHTML = falla;
	$('#myModalFalla').modal('hide');
	fallas.push(falla);

}

function datosJson(datos){  // funcion equipos
	$('#modalAltaE').modal('hide');
	if(datos.categoria === 'laptop')
	addServiceEquipo(datos.id);
}	

function enablePass(){
	valorRdio = $(this).val();
	selRad.push(valorRdio);
	if(valorRdio == 1)
		contraseña[tempId].disabled = false;
	else
		contraseña[tempId].disabled = true;
}

function fechaHoras(){

	$.datepicker.regional['es'] = {
        closeText: 'Cerrar',
        prevText: '<Ant',
        nextText: 'Sig>',
        currentText: 'Hoy',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
        dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
        weekHeader: 'Sm',
        dateFormat: 'dd/mm/yy',
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: ''
    };
    $.datepicker.setDefaults($.datepicker.regional['es']);

    $('#fechaInicio,#fechaFin ,#txtFechaProducto').datetimepicker({
		lang:'es',
		dateFormat : 'dd/mm/yy',
		hourMax : 19,
		hourMin: 9,
		showButtonPanel: false,
		constrainInput : true,
		beforeShowDay: noWeekends

	});

	$('#fechaFin').on('change',function(){
		var f = $('#fechaInicio').val();
		if($(this).val() <= f)
			$(this).css('background-color','#FFDDDD');
		else
			$(this).css('background-color','#FFF');
	});
	
	function noWeekends(date){
		var noWeekend = jQuery.datepicker.noWeekends(date);
		noWeekend[2] = 'No se permiten servicios en fin de semana';
		return noWeekend;
	}

}

function initTable(tabla){
	var btnLoad = $('.tblCli');
	//btnLoad = (tabla == '.tblCli')? tabla:'';
	$(tabla).dataTable({
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
	//console.log(btnLoad);
	btnLoad.on('click','tr .btnServicio',addServicio);
}

/*$.ajax({
		type:'POST',
		url:'/clientes/add_cliente/',
		//url:'add_cliente',
		data:$('#frmRegistro').serialize(),
		dataType: 'text',
		beforeSend:function(){
			$('#spnSpinnerR').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		},
		success:function(data){
			//$('#spnSpinnerR').html('Cliente agregado con éxito');
			//addTag(); // agregamos el elemento agregado al DOM
			//$('#txtCliente').val(data);
			addServicio(data);
		},
		error:function(xhr,estado,error){
				alert(error+' '+estado);
		},

		complete:function(xhr){
			$('#myModal').modal('hide');
			$('#modalAltaC').modal('hide');
			
		},
		timeout:10000

		
	});*/

function registro(){
	name = $('#txtNombre').val();
	tel = $('#txtTel').val();
	direc = $('#txtDir').val();
	if (validate(1)){

		$.post('/clientes/add_cliente/',$('#frmRegistro').serialize(),function(data){
			//$('#spnSpinnerR').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');delay
			addServicio(data);
		})

		.fail(function(){
			alert('Error! Consulte a su proveedor de sosftware');
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
function registroEquipo(){  // funcion equipos
	//alert($('#frmRegistroE').serialize());
	modEq = $('#txtModeloE').val();
	descEq =  $('#txtDescE').val();
	if(validate(3)){
		$.post('/add_equipo/',$('#frmRegistroE').serialize(),function(data){
			addServiceEquipo(data);
		})

		.fail(function(xhr){
			alert('Error! Consulte a su proveedor de software');
		});

	}
	else{
		alert('Olvidate ingresar algunos datos obligatorios');
		
		$('#txtModeloE, #txtDescE, #id_marca, #id_categoria').on('change',function(){
			$(this).css({
				'background-color':'white',
				'color':'black'

			});

		});
	}
	
}

function registroFalla(){
	nameF = $('#txtnameF').val();
	descF = $('#txtDescF').val();
	if(validate(2)){
		$.post('/add_falla/',$('#frmRegistroF').serialize(),function(datos){
			$('#modalAltaF').modal('hide');
			addServiceFalla(datos);
		})

		.fail(function(){
			alert('Error! Consulte a su proveedor de software');
		});

	}
	else{
		alert('Olvidate ingresar algunos datos obligatorios');
		$('.txtFalla , #txtDescF').on('change',function(){
			$(this).css({
				'background-color':'white',
				'color':'black'

			});

		});
	}
	
}	

function validate(value){

	switch(value){

		case 1:
			   return(validateCustomer());	
			   break;

		case 2:
			  return(validateFailure());	
			  break;

		case 3:
			  return(validateDevice());
			  break;		  	   
	}

	

}

function validateCustomer(){

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

function validateDevice(){
	if(!$('#id_marca').val() && !$('#id_categoria').val()){
		$('#id_marca').css({
			'background-color':'red',
			'color':'white'

		});
		$('#id_categoria').css({
			'background-color':'red',
			'color':'white'

		});
		
		$('#id_marca').focus();
		return false;

	}
	if(!$('#id_marca').val()){
		$('#id_marca').css({
			'background-color':'red',
			'color':'white'

		});
		$('#id_marca').focus();
		return false;

	}
	if(!$('#id_categoria').val()){
		$('#id_categoria').css({
			'background-color':'red',
			'color':'white'

		});
		
		$('#id_categoria').focus();
		return false;

	}
	if(modEq == '' && descEq == '' ){
		$('#txtModeloE').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtDescE').css({
			'background-color':'red',
			'color':'white'

		});
		
		$('#txtModeloE').focus();
		return false;
	}

	if(modEq == ''){
		$('#txtModeloE').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtModeloE').focus();
		return false;

	}

	if(descEq == ''){
		$('#txtDescE').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtDescE').focus();
		return false;

	}

	return true;

}

function validateFailure(){

	if(nameF == '' && descF == '' ){
		$('#txtnameF').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtDescF').css({
			'background-color':'red',
			'color':'white'

		});
		
		$('#txtnameF').focus();
		return false;
	}

	if(nameF == ''){
		$('#txtnameF').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtnameF').focus();
		return false;

	}

	if(descF == ''){
		$('#txtDescF').css({
			'background-color':'red',
			'color':'white'

		});
		$('#txtDescF').focus();
		return false;

	}

	return true;


}

function validaTipo(){
	if(tipoSer == 2){
		
		$('#txtDireccion').removeAttr('disabled');
		$('#fechaInicio,#fechaFin').removeAttr('disabled');

	}
}