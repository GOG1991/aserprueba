$(document).on('ready',function(){
 	var btnStep1=$('#btnStep1');
 	var date=new Date();
 	init(date);
 	
});

function init (date) {
	$( "#txtFecha" ).datepicker({showAnim: 'slideDown',setDate:new Date(),dateFormat:'d-mm-yy'});
	$('#txtFecha').val(date.getDate()+'-'+(date.getMonth()+1)+'-'+date.getFullYear());
}