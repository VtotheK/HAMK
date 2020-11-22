$(document).ready(function(){
	$("#contactFormId").submit(function(event){
		event.preventDefault();

		$.ajax({
			type: $("#contactFormId").attr("method"),
			url : $("#contactFormId").attr("action"),
			data : $("#contactFormId").serialize(),
			success: function(data)
			{
				alert("Yeah working");
				$("#contactFormName").val('');
				$("#contactFormMessage").val('');
				$("#contactFormEmail").val('');
			},
			error: function(data)
			{
				alert("You idiot");
			},
		});
	});
});


