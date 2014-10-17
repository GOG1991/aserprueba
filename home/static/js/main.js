 $(document).ready(function(){
 	//var link = $('.menu li a.link');
 	var servicios='';

 	$(window).scroll(function(){
   		if ($(this).scrollTop() > 10) {
        	$('.navbar').css({
        		'box-shadow':'0 4px 3px rgba(0,0,0,0.3)',
        	});
   		} 

   		else 
   		{
        	$('.navbar').css({
        		'box-shadow':'',
        	});
  	 	}

	});

 	$('#pop').popover({
 		placement : 'bottom',
 		html: 'true',
 		content :''
 	});

 	$('#servicioslist li').each(function(i,e){
 		//alert('posicion'+i+' '+$(e).text());
 		//'<a href="/servicios/detail_service/'+parseInt($(e).text())+'">Folio :+'+$(e).text()+ '</a><br>'
 		//servicios += 'folio'+' '+$(e).text() + ',';
 		servicios += '<a href="/servicios/detail_service/'+parseInt($(e).text())+'" class="lnknoti">Folio '+$(e).text()+ '</a><br>';

 	});
 	
 	$('#pop').attr('data-content',servicios);
 	//alert(servicios);
 	var ruta = window.location.pathname;
 	if(ruta == '/home/')
 		initTable();
 	var bolita = $('.lnkEdo');
 	$('.inicio').addClass('active-menu');
 	$("[rel='popover']").popover({
		placement : 'bottom',
		title : 'Notificaciones de servicios', 
		html: 'true', 
		content : '<div id="popOverBox">'+'<a href="/servicios/detail_service/'+1+'"><button class="btn btn-success btn-xs"><span class="glyphicon glyphicon-arrow-right"></span> </button></a>'+'</div>'
		});

 	//initTable();
 	$('.menu li').find('a.link').each(function(){
 		var href = $(this).attr('href');
 		if(href == ruta){
 			$(this).addClass('active-menu');
 			$('.inicio').removeClass('active-menu');
 		}

 	});

 	$('.lnkEdo').mouseover(estadosBolitas);
 	
              
 } );
function initTable () {
	$('#tblServicios').dataTable({
		//"aaSorting": [ [0,'desc'], [1,'asc'] ],
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

function estadosBolitas(){
	number = $(this).data('number');
	ball = $(this);
	
	$.ajax({
		type:'GET',
		url:'/servicios/contEdos/',
		data : {'id':number},
		success:function(resp){
			//$('.btnFront').text(resp);
			if(parseInt(resp) > 9999)
				ball.attr('title',resp);

			ball.children('div:first').text(resp);

		},

		error:function(xhr,estado,error){
				alert(error+' '+estado);
		},

		complete:function(xhr){
			
		},

		timeout:10000

	})
}



