$(function(){
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
			$('.divAccesorios').html(datos);
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