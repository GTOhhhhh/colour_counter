$(document).ready(function() {
		$('.custom-file-input').on('change',function(){
			console.log('change');
			$(this).next('.custom-file-label').addClass("selected").html($(this).val());
		});
	
});