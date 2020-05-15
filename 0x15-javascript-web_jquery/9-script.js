let url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, function (data) {
	$('div#hello').text(data.hello) }
);
