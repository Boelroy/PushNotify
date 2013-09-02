$('.collapse ul.nav li a').click(function(){
	var active_one = this;
	var action_type = $(this).attr('title');
	$.ajax({
		url: action_type,
		data: {'action':action_type},
		type: 'get',
		success: function(data){
			if(action_type=="start")
				$.getScript("static/js/notify.js")
			else
				$.getScript("static/js/users.js")
			$.each($('ul.nav li'), function(){
				$(this).removeClass('active');
			});
			$(active_one).parent().addClass('active');
			$('section').replaceWith(data)
		},
	})
});