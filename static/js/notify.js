
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

$('ul.nav li a').click(function(){
	var active_one = this;
	var action_type = $(this).attr('title');
	$.ajax({
		url: '/'+action_type,
		data: {'action':action_type},
		type: 'get',
		success: function(data){
			$.getScript("static/js/users.js")
			$.each($('ul.nav li'), function(){
				$(this).removeClass('active');
			});
			$(active_one).parent().addClass('active');
			$('section').replaceWith(data)
			$.getScript("static/js/notify.js")
		}
	})
});
