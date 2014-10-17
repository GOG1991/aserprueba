var total;
var first;
var idS;
var costo;
var costoR;
var costoD;
var btnEntrega;
$(function(){
	idS = $('#txtIdS').val();
	btnE = $('#btnEnt');
	btnEntrega = $('#btnEntrega');
	totalP = parseInt($('#spnTotal').text());

	$('#modalSalida').modal({
		show:false,
		backdrop:true,
		keyboard:true,
	});

	/*total = document.getElementById('spnToSer');
	first = parseInt($('#spnTotal').text());
	sumTot();
	$('#txtCosto').on('change',function(){
		first += parseInt($(this).val());
		sumTot();
	});
	$('#txtRespaldo').on('change',function(){
		first += parseInt($(this).val());
		sumTot();
	});*/
	//probando btnE.on('click',confirmacion);
	btnE.on('click',costos);
	
});

function confirmacion(){
	//e.preventDefault();
	isNaN(parseInt($('#txtCostoS').val())) ? costo = 0: costo = parseInt($('#txtCostoS').val());
	//costo = parseInt($('#txtCostoS').val());
	isNaN(parseInt($('#txtCostoR').val())) ? costoR = 0: costoR = parseInt($('#txtCostoR').val());
	isNaN(parseInt($('#txtDesc').val())) ? costoD = 0: costoD = parseInt($('#txtDesc').val());

	if(costoD > 0){
		costoD = costoD/100;
		total = costo + costoR + totalP;
		total = total - (total * costoD);
	}
	else
		total = costo + costoR + totalP;

	//costoR = parseInt($('#txtCostoR').val());
	

	//$('#costoProd').text(totalP);
	//$('#costoServi').text(costo);
	//$('#costoResp').text(costoR);
	$('#totalCosto').text(total);
	$('#divFin').slideDown('slow');
	//$('#modalSalida').modal('show');
	//btnEntrega.on('click',costos);
}

function costos(e){
	e.preventDefault();
	$.ajax({
		type:'POST',
		url:'/servicios/costos/',
		data:$('#frmSalida').serialize(),
		dataType:'text',
		beforeSend:function(){
			$('#spnCalc').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		},
		success:function(response){
			confirmacion();
			//changeEdo();
			/*window.setTimeout(function(){
				window.location.href = '/home/';
			},1300);*/
		},
		error:function(xhr,estado,error){
			alert(error+' '+estado+' '+'En los costos , consulte a su proveedor de software');
		},
		complete:function(xhr){
			//$('#modalSalida').modal('hide');
			$('#spnCalc').html('');	

		},
		timeout:10000

	});

}

function changeEdo(){  // funcion que cambia el estado a entregado , omitida

	$.ajax({

		type:'POST',
		url:'/servicios/estadofin/',
		data:$('#frmEdoFin').serialize(),
		dataType:'text',
		beforeSend:function(){
			
		},
		success:function(response){
			
		},
		error:function(xhr,estado,error){
			alert(error+' '+estado+' '+' En el cambio de estado , consulte a su proveedor de software');
		},
		complete:function(xhr){
			

		},
		timeout:10000

	});

}

function sumTot(){
	total.innerHTML  = first;

}