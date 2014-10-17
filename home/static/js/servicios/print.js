$(function(){
	var n;

	$('#btnSerR').on('click',function(){
		n = parseInt($(this).data('id'));
		show(n);
		
	});

	$('#btnSerE').on('click',function(){
		n = parseInt($(this).data('id'));
		show(n);
		
	});

	function show(valor){
		$('#spnwait').html('<i class="fa fa-spinner fa-spin fa-lg"></i>');
		window.setTimeout(function(){
			
			$('#spnwait').html('');

		},200);

	
		if(n == 1){
			$('#printR').slideToggle('slow');
		}
		else if(n == 2)
			$('#printE').slideToggle('slow');
		else
			alert('error consulte a su proveedor de software');
		
	}

});