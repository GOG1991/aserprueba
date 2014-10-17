var valor;
var btnSug;
$(function(){
	var estado = $('#lnkEdo');
	var prod = $('#lnkprod');
	var sol = $('#btnSol');
	var addSol = $('#btnaddSol');
	var fProd = $('#btnFormP');
	var his = $('#lnkHis');
	var hisE = $('.btnHist');
	var dS = $('.lnkSol');
	btnSug = $('#btnaddSolPo');
	valor = $('#idSer').val();
	$('#spnSol').html('');
	$('#spinProdExito').html('');
	var p = document.getElementsByClassName('btnDetalles');

	$('#btnOpenG').on('click',function(){
		$('#changeG').slideToggle();
	});
	$('#btnChangeG').on('click',changeGar);

	$('#modalChangeEdo').modal({
		show:false,
		backdrop:true,
		keyboard:true,
	});
	$('#modalProd').modal({
		show:false,
		backdrop:true,
		keyboard:true,
	});

	$('#modalSol').modal({
		show:false,
		backdrop:true,
		keyboard:true,
	});
	$('#moaddProd').modal({
		show:false,
		backdrop:true,
		keyboard:true,
	});
	$('#modalH').modal({
		show:false,
		backdrop:true,
		keyboard:true,
	});
	$('#modalSol').modal({
		show:false,
		backdrop:true,
		keyboard:true,
	});

	addSol.on('click',addSolView);
	prod.on('click',selProd);
	estado.on('click',changeEdo);
	sol.on('click',soluciones);
	fProd.on('click',addProd);
	his.on('click',historialEdos);
	hisE.on('click',historialEq);
	dS.on('click',detailSolucion);
	btnSug.on('click',sugerencias);
	$('#btnRsolucion').on('click',agregarSolBd);
	$('#btnaddProd').on('click',addProdBD);


	$('.btnDetalles').on('click',function(){
		n = $(this).data('idequipo');
		elm = $(this);
		$.ajax({
			type:'GET',
			url:'/listac/',
			data:{'id':n},
			dataType:'text',
			beforeSend:function(){

			},
			success:function(datos){
				elm.parent().find('.divAccesorios').html(datos);
				//$('.divAccesorios').html(datos);
				elm.parent().find('.divAccesorios').slideToggle();
			},
			error:function(xhr,estado,error){
				alert(error+' '+estado);
			},

			complete:function(xhr){
				
				
			},
			timeout:10000
		});

	});

});

function addProd(e){
	e.preventDefault();
	$.ajax({

		type:'GET',
		url:'/servicios/add_productos/',
		beforeSend:function(){

		},
		success:function(response){
			$('#divAddprod').html(response);
			$('#moaddProd').modal('show');
		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			
		},
		timeout:10000

	});


}

function addProdBD(e){
	e.preventDefault();
	$.ajax({
		type:'POST',
		dataType:'text',
		url:'/servicios/add_productos/',
		data:$('#frmaddPnew').serialize(),
		beforeSend:function(){
			$('#spnProdBd').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		},
		success:function(data){
			$('#spinProdExito').html('Producto agregado');

		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			$('#moaddProd').modal('hide');
			$('#spnProdBd').html('');
		},
		timeout:10000
	});

}

function addSol(){
	$.ajax({
		type:'POST',
		url:'/servicios/solucion/',
		data:$('#frmSol').serialize(),
		beforeSend:function(){
			$('#spinSol').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		},
		success:function(response){
			$('#spinSol').html('<span style="font-weight:bold;">Soluciones agregadas la página se refrescara automáticamente</span>');
			window.setTimeout(function(){
				window.location.href = '/servicios/detail_service/'+valor;
			},1300);
		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			
		},
		timeout:10000


	});
	
}

function addSolView(e){
	e.preventDefault();
	$.ajax({
		type:'GET',
		url:'/add_sol/',
		beforeSend:function(){

		},
		success:function(data){
			$('#modalSol').modal('show');
			$('#addSol').html(data);

		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			
		},
		timeout:10000
	});
}

function agregarProd(e){
	e.preventDefault();
	
	$.ajax({
		type:'POST',
		url:'/servicios/selprod/',
		data:$('#frmProd').serialize(),
		dataType: 'text',
		beforeSend:function(){
			$('#spnProd').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		},
		success:function(data){
			var elemento = '<li>'+data+'</li>';
			$('#listprod').prepend($(elemento).fadeIn('slow'));

		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			$('#modalProd').modal('hide');
			
		},
		timeout:10000


	});

}

function agregarSolBd(e){
	e.preventDefault();
	$.ajax({
		type:'POST',
		dataType:'text',
		url:'/add_sol/',
		data:$('#frmSolBd').serialize(),
		beforeSend:function(){
			$('#spnSolBd').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		},
		success:function(data){
			$('#spnSol').html('Solución agregada');

		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			$('#modalSol').modal('hide');
			$('#spnSolBd').html('');
		},
		timeout:10000
	});
}

function change(e){
	e.preventDefault();
	ruta = $('#frmEstados').attr('action');
	if($('#txtRazon').val().length < 1){
		$('#txtRazon').css('background','#FFDDDD');
		alert('Debes escribir la razón del cambio de estado');
	}
	else{

			$.ajax({
				type:'POST',
				url:ruta,
				data:$('#frmEstados').serialize(),
				dataType: 'text',
				beforeSend:function(){
					$('#spnEdos').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
				},
				success:function(data){
					$('#lastEdo').html(data);
					
				},
				error:function(xhr,estado,error){
						alert(error+' '+estado);
				},
				complete:function(xhr){
					$('#modalChangeEdo').modal('hide');
					$('#spnEdos').html('');
					
				},
				timeout:1000

			});

		}
	
}

function changeEdo(){
	valor = $('#idSer').val();
	$('#modalChangeEdo').modal('show');
	$.ajax({
		type:'GET',
		url:'/servicios/detail_servic/cambio_edo/',
		data:{'id':valor},
		beforeSend:function(){

		},
		success:function(data){
			$('#divEdos').html(data);
			$('#txtRazon').on('click',function(){
				$(this).css('background','#fff');
			});
			$('#cambiar').on('click',change);

		},
		error:function(xhr){
			alert(xhr);
		},
		timeout:10000

	});
}

function changeGar(e){
	e.preventDefault();
	$.ajax({

		type:'POST',
		url:'/servicios/cambiarGar/',
		data:$('#frmChangeG').serialize(),
		dataType:'text',
		beforeSend:function(){
			$('#msj-gar').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		},
		success:function(response){
			$('#spn-diasG').html('<strong>'+response+'</strong>');
		},
		error:function(xhr){
			alert(xhr + 'Error , ponte en contacto con el proveedor de software');
		},
		complete:function(){
			$('#msj-gar').html('');
			$('#changeG').slideToggle('slow');

		},
		timeout:10000


	});
}

function historialEdos(e){
	e.preventDefault();

	$.ajax({
		type:'GET',
		url:'/servicios/detail_service/estados/',
		data:{'id':valor},
		dataType:'text',
		beforeSend:function(){

		},
		success:function(response){
			$('#modalH').modal('show');
			$('#Historial').html(response);
		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			
		},
		timeout:10000


	});
	$('#modalH').modal('show');


}

function detailSolucion(e){ //dante
	e.preventDefault();
	n = $(this).data('idsolucion');

	$.ajax({
		type:'GET',
		url:'/detail_solucion/',
		data:{'id':n},
		beforeSend:function(){

		},
		success:function(response){
			$('#modalDetail').modal('show');
			$('#soluciones').html(response);
		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			
		},
		timeout:10000


	});
	$('#modalDetail').modal('show');


}

function historialEq(e){
	e.preventDefault();
	n = $(this).data('idequipo');
	elm = $(this);
	$.ajax({
		type:'GET',
		url:'/servicios/detail_equipo/',
		data:{'id':n},
		beforeSend:function(){

		},
		success:function(data){
			elm.parent().find('.divHistorial').html(data);
				//$('.divAccesorios').html(datos);
			elm.parent().find('.divHistorial').slideToggle();

		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			
		},
		timeout:10000

	});
}

function selProd(e){
	e.preventDefault();
	
	$.ajax({
		type:'GET',
		url:'/servicios/selprod/',
		beforeSend:function(){

		},
		success:function(data){
			$('#divProd').html(data);
			$('#slctProducto option:nth-child(2)').attr('selected','true');
			$('#modalProd').modal('show');
			$('#btnProd').on('click',agregarProd);

		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			
		},
		timeout:10000


	});
}

function soluciones(e){
	var valor = $('#idSer').val();
	e.preventDefault();
	$.ajax({
		type:'GET',
		url:'/servicios/solucion/',
		data:{'id':valor},
		beforeSend:function(){

		},
		success:function(response){
			$('#divSol').html(response);
			$('#divSol').slideToggle('slow');
			$('#btnAddSol').on('click',function(e){
				e.preventDefault();
				addSol();
			});

		},
		error:function(xhr){
			alert(xhr);
		},
		complete:function(){
			
		},
		timeout:10000


	});
	
}

function sugerencias(e){
	e.preventDefault();
	$('#divSolPosi').slideToggle();

}