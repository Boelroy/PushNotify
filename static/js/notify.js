
$('#submit').click(function(){
	$('#submit').button('loading')
	$.ajax({
		url: '/notify',
		data: $('#notify').serialize(),
		type: 'get',
		success: function(data){
			$("#msg").removeClass("hide");
			$("#submit").button('complete')
		}
	})
});

