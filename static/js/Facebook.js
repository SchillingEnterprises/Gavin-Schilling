$(document)
	.ready(function() {
		$.ajaxSetup({
			cache: true
		});
		$.getScript(
			'//connect.facebook.net/en_US/sdk.js',
			function() {
				FB.init({
					appId: '561430954040905',
					version: 'v2.7'
				});
				$('#loginbutton,#feedbutton')
					.removeAttr('disabled');
				FB.getLoginStatus(updateStatusCallback);
			});
	});
(function(d, s, id) {
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id))
		return;
	js = d.createElement(s);
	js.id = id;
	js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.7&appId=561430954040905";
	fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
window.fbAsyncInit = function() {
	FB.init({
		appId: '561430954040905',
		xfbml: true,
		version: 'v2.7'
	});
};
(function(d, s, id) {
	var js, fjs = d
		.getElementsByTagName(s)[0];
	if (d.getElementById(id)) {
		return;
	}
	js = d.createElement(s);
	js.id = id;
	js.src = "//connect.facebook.net/en_US/sdk.js";
	fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));